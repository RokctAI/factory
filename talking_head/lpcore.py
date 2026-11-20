"""Thin LivePortrait helper: load the models once, then render the portrait with an
edited expression (mouth, smile, blink, brows, gaze, head pose).

The expression edits follow ComfyUI-AdvancedLivePortrait's ExpressionEditor.
LP_SRC must point at a LivePortrait checkout with its pretrained_weights/."""
import os, sys
import numpy as np, cv2, torch

LP = os.environ['LP_SRC']
sys.path.insert(0, LP)
_cwd = os.getcwd(); os.chdir(LP)   # LivePortrait resolves its weights relative to the cwd
from src.config.inference_config import InferenceConfig
from src.config.crop_config import CropConfig
from src.live_portrait_wrapper import LivePortraitWrapper
from src.utils.cropper import Cropper
from src.utils.crop import prepare_paste_back, paste_back
os.chdir(_cwd)
torch.set_num_threads(int(os.environ.get('TORCH_THREADS', os.cpu_count() or 4)))


class Face:
    def __init__(self, img_path):
        img_path = os.path.abspath(img_path)
        cwd = os.getcwd(); os.chdir(LP)
        try:
            icfg = InferenceConfig(flag_force_cpu=True, flag_use_half_precision=False, flag_stitching=True)
            ccfg = CropConfig(flag_force_cpu=True)
            self.w = LivePortraitWrapper(icfg)
            self.cropper = Cropper(crop_cfg=ccfg, flag_force_cpu=True)
            mask = cv2.imread(os.path.join(LP, 'src/utils/resources/mask_template.png'), cv2.IMREAD_COLOR)
        finally:
            os.chdir(cwd)
        img = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)
        self.img = img
        self.crop = self.cropper.crop_source_image(img, ccfg)
        if self.crop is None:
            raise SystemExit(f'no face found in {os.path.basename(img_path)}')
        x = self.w.prepare_source(self.crop['img_crop_256x256'])
        self.kp = self.w.get_kp_info(x)
        self.f3d = self.w.extract_feature_3d(x)
        self.x_s = self.w.transform_keypoint(self.kp)
        self.mask = prepare_paste_back(mask, self.crop['M_c2o'], dsize=(img.shape[1], img.shape[0]))

    def view_box(self, width_faces=1.05):
        """Head-and-shoulders 3:4 box around the face, in card pixels."""
        M = self.crop['M_c2o']
        cx, cy = M[:2, :2] @ np.array([256, 256]) + M[:2, 2]
        side = np.linalg.norm(M[:2, 0]) * 512
        H, W = self.img.shape[:2]
        cw = min(W, int(side * width_faces)) // 2 * 2; ch = min(H, int(cw * 4 / 3)) // 2 * 2
        x0 = int(np.clip(cx - cw / 2, 0, W - cw)); y0 = int(np.clip(cy - ch * 0.42, 0, H - ch))
        return x0, y0, x0 + cw, y0 + ch

    def render(self, aaa=0, eee=0, woo=0, smile=0, blink=0, brow=0, look_x=0, look_y=0,
               pitch=0, yaw=0, roll=0, crop_only=False):
        e = self.kp['exp'].clone()
        # smile
        e[0,20,1]+=smile*-0.01; e[0,14,1]+=smile*-0.02; e[0,17,1]+=smile*0.0065; e[0,17,2]+=smile*0.003
        e[0,13,1]+=smile*-0.00275; e[0,16,1]+=smile*-0.00275; e[0,3,1]+=smile*-0.0035; e[0,7,1]+=smile*-0.0035
        # aaa: jaw open
        e[0,19,1]+=aaa*0.001; e[0,19,2]+=aaa*0.0001; e[0,17,1]+=aaa*-0.0001
        pitch = pitch - aaa*0.05
        # eee: lips spread
        e[0,20,2]+=eee*-0.001; e[0,20,1]+=eee*-0.001; e[0,14,1]+=eee*-0.001
        # woo: lips rounded
        e[0,14,1]+=woo*0.001; e[0,3,1]+=woo*-0.0005; e[0,7,1]+=woo*-0.0005; e[0,17,2]+=woo*-0.0005
        # brows (+ raise)
        if brow > 0: e[0,1,1]+=brow*0.001; e[0,2,1]+=brow*-0.001
        else: e[0,1,0]+=brow*-0.001; e[0,2,0]+=brow*0.001; e[0,1,1]+=brow*0.0003; e[0,2,1]+=brow*-0.0003
        # gaze (look_x + right, look_y + up)
        if look_x > 0: e[0,11,0]+=look_x*0.0007; e[0,15,0]+=look_x*0.001
        else: e[0,11,0]+=look_x*0.001; e[0,15,0]+=look_x*0.0007
        e[0,11,1]+=look_y*-0.001; e[0,15,1]+=look_y*-0.001
        blink = blink - look_y/2.
        # blink (negative closes)
        e[0,11,1]-=blink*0.001; e[0,13,1]+=blink*0.0003; e[0,15,1]-=blink*0.001; e[0,16,1]+=blink*0.0003
        e[0,1,1]+=blink*-0.00025; e[0,2,1]+=blink*0.00025
        kp = dict(self.kp); kp['exp'] = e
        kp['pitch'] = self.kp['pitch'] + pitch; kp['yaw'] = self.kp['yaw'] + yaw; kp['roll'] = self.kp['roll'] + roll
        x_d = self.w.stitching(self.x_s, self.w.transform_keypoint(kp))
        out = self.w.warp_decode(self.f3d, self.x_s, x_d)
        crop = self.w.parse_output(out['out'])[0]
        if crop_only:
            return crop
        return paste_back(crop, self.crop['M_c2o'], self.img, self.mask)
