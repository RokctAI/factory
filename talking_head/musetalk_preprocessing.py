"""CPU-friendly stand-in for MuseTalk's preprocessing: uses the insightface detector
(already present for LivePortrait) instead of mmpose/DWPose + face_alignment, which
don't install on this Python. Same box rule: from mid-nose up by the nose-to-chin
distance, down to the chin."""
import os, sys, numpy as np, cv2
from tqdm import tqdm
LP = os.environ["LP_SRC"]
sys.path.insert(0, LP)
from src.utils.face_analysis_diy import FaceAnalysisDIY
fa = FaceAnalysisDIY(name='buffalo_l', root=os.path.join(LP, 'pretrained_weights/insightface'), providers=['CPUExecutionProvider'])
fa.prepare(ctx_id=-1, det_size=(512, 512))
coord_placeholder = (0.0, 0.0, 0.0, 0.0)

def read_imgs(img_list):
    return [cv2.imread(p) for p in tqdm(img_list)]

def get_landmark_and_bbox(img_list, upperbondrange=0):
    frames = read_imgs(img_list); coords = []
    for fr in tqdm(frames):
        faces = fa.get(fr, flag_do_landmark_2d_106=True)
        if not faces: coords.append(coord_placeholder); continue
        f = faces[0]; lm = f.landmark_2d_106
        x1, x2 = int(lm[:, 0].min()), int(lm[:, 0].max()); chin = int(lm[:, 1].max())
        eyes_y = f.kps[:2, 1].mean(); nose_y = f.kps[2, 1]
        mid = (eyes_y + nose_y) / 2 + upperbondrange
        y1 = int(max(0, mid - (chin - mid)))
        coords.append((x1, y1, x2, chin))
    return coords, frames
