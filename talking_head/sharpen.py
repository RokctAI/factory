"""Sharpen the mouth of a talking-face clip with GFPGAN v1.4 (Apache-2.0).

MuseTalk draws lips at 256x256, so they look soft when the face is shown large.
Each frame: find the face's five points, align it to the 512 FFHQ template,
restore it, and paste back ONLY the lower face (mouth, chin) with a soft mask,
so the eyes and identity stay exactly as LivePortrait drew them.

  python sharpen.py in.mp4 out.mp4
Needs LP_SRC (insightface detector weights) and GFPGAN_WEIGHTS (GFPGANv1.4.pth).
GFPGAN's clean architecture is loaded straight from the installed `gfpgan`
package (installed --no-deps); its two small imports from basicsr are stubbed,
because basicsr does not build on current Python/torch."""
import os, sys, types, importlib.util, time
import numpy as np, cv2, torch
from torch import nn

LP = os.environ['LP_SRC']
sys.path.insert(0, LP)
from src.utils.face_analysis_diy import FaceAnalysisDIY

FFHQ5 = np.array([[192.98138, 239.94708], [318.90277, 240.1936], [256.63416, 314.01935],
                  [201.26117, 371.41043], [313.08905, 371.15118]], np.float32)


def _stub_basicsr():
    reg = types.SimpleNamespace(register=lambda *a, **k: (lambda c: c))

    @torch.no_grad()
    def default_init_weights(module_list, scale=1, bias_fill=0, **kwargs):
        for module in (module_list if isinstance(module_list, list) else [module_list]):
            for m in module.modules():
                if isinstance(m, (nn.Conv2d, nn.Linear)):
                    nn.init.kaiming_normal_(m.weight, **kwargs); m.weight.data *= scale
                    if m.bias is not None:
                        m.bias.data.fill_(bias_fill)
    for name, attrs in {'basicsr': {}, 'basicsr.utils': {}, 'basicsr.archs': {},
                        'basicsr.utils.registry': {'ARCH_REGISTRY': reg},
                        'basicsr.archs.arch_util': {'default_init_weights': default_init_weights}}.items():
        mod = sys.modules.setdefault(name, types.ModuleType(name))
        for k, v in attrs.items():
            setattr(mod, k, v)


def load_gfpgan(weights):
    _stub_basicsr()
    # find_spec only locates the package: gfpgan/__init__ (which pulls in
    # basicsr's data and model code) is never run.
    archs = os.path.join(os.path.dirname(importlib.util.find_spec('gfpgan').origin), 'archs')
    pkg = types.ModuleType('gfpgan_clean'); pkg.__path__ = [archs]; sys.modules['gfpgan_clean'] = pkg
    for name in ('stylegan2_clean_arch', 'gfpganv1_clean_arch'):
        spec = importlib.util.spec_from_file_location(f'gfpgan_clean.{name}', os.path.join(archs, f'{name}.py'))
        mod = importlib.util.module_from_spec(spec); sys.modules[spec.name] = mod; spec.loader.exec_module(mod)
    m = sys.modules['gfpgan_clean.gfpganv1_clean_arch'].GFPGANv1Clean(
        out_size=512, num_style_feat=512, channel_multiplier=2, decoder_load_path=None, fix_decoder=False,
        num_mlp=8, input_is_latent=True, different_w=True, narrow=1, sft_half=True)
    sd = torch.load(weights, map_location='cpu', weights_only=True)
    m.load_state_dict(sd['params_ema'] if 'params_ema' in sd else sd['params']); m.eval()
    return m


def main(src, dst):
    torch.set_num_threads(int(os.environ.get('TORCH_THREADS', os.cpu_count() or 4)))
    fa = FaceAnalysisDIY(name='buffalo_l', root=os.path.join(LP, 'pretrained_weights/insightface'),
                         providers=['CPUExecutionProvider'])
    fa.prepare(ctx_id=-1, det_size=(512, 512))
    net = load_gfpgan(os.environ['GFPGAN_WEIGHTS'])
    yy, xx = np.mgrid[0:512, 0:512]
    mask = (((xx - 256) / 150.) ** 2 + ((yy - 390) / 115.) ** 2 <= 1).astype(np.float32)
    mask = cv2.GaussianBlur(mask, (0, 0), 18)
    cap = cv2.VideoCapture(src); fps = cap.get(cv2.CAP_PROP_FPS)
    W, H = int(cap.get(3)), int(cap.get(4))
    out = cv2.VideoWriter(dst, cv2.VideoWriter_fourcc(*'mp4v'), fps, (W, H))
    n = 0; t0 = time.time()
    while True:
        ok, f = cap.read()
        if not ok:
            break
        faces = fa.get(f)
        if faces:
            kps = faces[0]['kps'] if isinstance(faces[0], dict) else faces[0].kps
            A, _ = cv2.estimateAffinePartial2D(kps.astype(np.float32), FFHQ5, method=cv2.LMEDS)
            crop = cv2.warpAffine(f, A, (512, 512), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
            x = torch.from_numpy(cv2.cvtColor(crop, cv2.COLOR_BGR2RGB).transpose(2, 0, 1)).float()[None] / 255.
            with torch.no_grad():
                y = net((x - 0.5) / 0.5, return_rgb=False, weight=0.5)[0]
            r = ((y[0].clamp(-1, 1) + 1) / 2 * 255).permute(1, 2, 0).numpy().astype(np.uint8)
            r = cv2.cvtColor(r, cv2.COLOR_RGB2BGR).astype(np.float32)
            Ai = cv2.invertAffineTransform(A)
            rb = cv2.warpAffine(r, Ai, (W, H), flags=cv2.INTER_LINEAR)
            mb = cv2.warpAffine(mask, Ai, (W, H))[..., None]
            f = (f * (1 - mb) + rb * mb).clip(0, 255).astype(np.uint8)
        out.write(f); n += 1
    out.release()
    print(f'sharpened {n} frames, {(time.time() - t0) / max(n, 1):.1f} s/frame')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
