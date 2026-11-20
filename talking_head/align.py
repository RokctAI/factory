"""Letter timings for a spoken line: forced alignment of the known text to the audio
(torchaudio MMS_FA). Writes [[letter, start_s, end_s], ...]."""
import sys, json, argparse
import torch, soundfile as sf
from torchaudio.pipelines import MMS_FA as bundle


def align(wav16k, text):
    d, sr = sf.read(wav16k, dtype='float32')
    if d.ndim > 1: d = d.mean(1)
    wav = torch.from_numpy(d)[None]
    words = [''.join(c for c in w.lower() if 'a' <= c <= 'z') for w in text.replace('-', ' ').split()]
    words = [w for w in words if w]
    model = bundle.get_model(with_star=False); tok = bundle.get_tokenizer(); al = bundle.get_aligner()
    with torch.inference_mode():
        em, _ = model(wav)
    spans = al(em[0], tok(words))
    ratio = wav.shape[1] / em.shape[1] / sr
    return [[ch, round(s.start * ratio, 3), round(s.end * ratio, 3)]
            for w, sp in zip(words, spans) for ch, s in zip(w, sp)]


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('wav16k'); ap.add_argument('text_file'); ap.add_argument('out')
    a = ap.parse_args()
    out = align(a.wav16k, open(a.text_file, encoding='utf-8').read())
    json.dump(out, open(a.out, 'w'))
    print(f'aligned {len(out)} letters')   # counts only: the line's text stays out of public logs
