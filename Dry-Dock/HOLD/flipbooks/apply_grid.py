#!/usr/bin/env python3
"""
Grid JSON → Frame Extractor.

Reads grid_XX.json files exported from the visual segmenter tool.
Each JSON contains exact pixel coordinates for every cell.
Cuts frames, auto-trims, pads to square, exports MP4/GIF/viewer.

Usage:
  python3 apply_grid.py grid_00.json
  python3 apply_grid.py grid_00.json grid_01.json grid_02.json ...
  python3 apply_grid.py  (processes all grid_*.json in flipbooks/)
"""
import os, sys, json, glob
import numpy as np
from PIL import Image
import imageio

HOLD = '/Users/gaia/OPERATION-DESCRIBE/Dry-Dock/HOLD'
FLIPBOOKS = os.path.join(HOLD, 'flipbooks')

# Map sheet ID to source image path
IMAGE_MAP = {
    '00': '00-the-shield.png',
    '01': '01-Construction-and-Cosmic-Design/01-cosmic-gemini.png',
    '02': '02-Two-Cities-Peace-and-Law/02-bride-law-Gemini_Generated_Image_6oi6ce6oi6ce6oi6.jpeg',
    '03': '03-Two-Cities-War-and-Ambush/Gemini_Generated_Image_2ylbjn2ylbjn2ylb.jpeg',
    '04': '04-Labors-of-the-Field/Gemini_Generated_Image_ffbktcffbktcffbk.jpeg',
    '05': '05-Cattle-Lions-and-Sheep/Gemini_Generated_Image_5kxfd95kxfd95kxf.jpeg',
    '06': '06-Dance-and-Ocean-Rim/06-dance.png',
}

DIR_MAP = {
    '00': '00-whole-shield-gemini',
    '01': '01-cosmic-gemini',
    '02': '02-peace-law-gemini',
    '03': '03-war-ambush-gemini',
    '04': '04-labors-gemini',
    '05': '05-cattle-gemini',
    '06': '06-dance-gemini',
}

# Infer sheet ID from filename if sheet is 'custom'
def infer_sheet_id(grid_path, grid_data):
    sid = grid_data.get('sheet', 'custom')
    if sid != 'custom':
        return sid
    fname = os.path.basename(grid_path).lower()
    for key in ['00', '01', '02', '03', '04', '05', '06']:
        if key in fname:
            return key
    # Try name matching
    name_map = {'shield':'00','cosmic':'01','peace':'02','war':'03','labor':'04','cattle':'05','lion':'05','dance':'06'}
    for word, key in name_map.items():
        if word in fname:
            return key
    return sid


def auto_trim(img, padding=2):
    arr = np.array(img.convert('L'), dtype=float)
    H, W = arr.shape
    if H < 10 or W < 10:
        return img
    ring = np.concatenate([arr[0:3,:].ravel(), arr[-3:,:].ravel(),
                           arr[:,0:3].ravel(), arr[:,-3:].ravel()])
    bg = np.median(ring)
    mask = np.abs(arr - bg) > 20
    if not mask.any():
        return img
    rows = mask.any(axis=1)
    cols = mask.any(axis=0)
    if not rows.any() or not cols.any():
        return img
    y0 = max(0, int(np.argmax(rows)) - padding)
    y1 = min(H, int(H - np.argmax(rows[::-1])) + padding)
    x0 = max(0, int(np.argmax(cols)) - padding)
    x1 = min(W, int(W - np.argmax(cols[::-1])) + padding)
    if x1 - x0 < 8 or y1 - y0 < 8:
        return img
    return img.crop((x0, y0, x1, y1))


def process_grid(grid_path):
    with open(grid_path) as f:
        grid = json.load(f)
    
    sid = infer_sheet_id(grid_path, grid)
    if sid not in IMAGE_MAP:
        print(f'  ⚠ Unknown sheet ID: {sid}')
        return 0
    
    img_path = os.path.join(HOLD, IMAGE_MAP[sid])
    out_dir = os.path.join(FLIPBOOKS, DIR_MAP[sid])
    
    if not os.path.exists(img_path):
        print(f'  ⚠ Image not found: {img_path}')
        return 0
    
    img = Image.open(img_path).convert('RGB')
    cells = grid['cells']
    
    os.makedirs(os.path.join(out_dir, 'frames'), exist_ok=True)
    
    # Skip title cell (row 0, col 0) for sheets that have one
    skip_title = True
    
    manifest = []
    idx = 0
    
    for cell in cells:
        if skip_title and cell['row'] == 0 and cell['col'] == 0:
            continue
        
        x, y, w, h = cell['x'], cell['y'], cell['w'], cell['h']
        if w < 5 or h < 5:
            continue  # skip degenerate cells (from gutter insets)
        # Clamp to image bounds
        x = max(0, x); y = max(0, y)
        w = min(w, img.width - x); h = min(h, img.height - y)
        if w < 5 or h < 5:
            continue
        crop = img.crop((x, y, x + w, y + h))
        trimmed = auto_trim(crop, padding=2)
        
        tw, th = trimmed.size
        sz = max(tw, th)
        sq = Image.new('RGB', (sz, sz), (255, 255, 255))
        sq.paste(trimmed, ((sz - tw) // 2, (sz - th) // 2))
        
        path = os.path.join(out_dir, 'frames', f'frame_{idx:03d}.png')
        sq.save(path)
        manifest.append({'index': idx, 'row': cell['row'], 'col': cell['col'],
                         'bbox': [x, y, x+w, y+h], 'path': f'frames/frame_{idx:03d}.png'})
        idx += 1
    
    # Clean stale frames
    for f in os.listdir(os.path.join(out_dir, 'frames')):
        if f.startswith('frame_'):
            n = int(f.split('_')[1].split('.')[0])
            if n >= idx:
                os.remove(os.path.join(out_dir, 'frames', f))
    
    with open(os.path.join(out_dir, 'manifest.json'), 'w') as f:
        json.dump(manifest, f, indent=2)
    
    # Export MP4
    os.system(f'ffmpeg -y -framerate 6 -i "{out_dir}/frames/frame_%03d.png" '
              f'-vf "scale=512:512:flags=lanczos" '
              f'-c:v libx264 -pix_fmt yuv420p -crf 18 "{out_dir}/flipbook.mp4" 2>/dev/null')
    
    # Export GIF
    frames = []
    for i in range(idx):
        im = Image.open(os.path.join(out_dir, 'frames', f'frame_{i:03d}.png'))
        im = im.resize((256, 256), Image.LANCZOS)
        frames.append(np.array(im))
    imageio.mimsave(os.path.join(out_dir, 'flipbook.gif'), frames, duration=167, loop=0)
    
    return idx


# ── MAIN ──
if len(sys.argv) > 1:
    grid_files = sys.argv[1:]
else:
    # Search both flipbooks/ and segments/
    grid_files = sorted(
        glob.glob(os.path.join(FLIPBOOKS, 'grid_*.json')) +
        glob.glob(os.path.join(HOLD, 'segments', '*.json'))
    )

if not grid_files:
    print('No grid JSON files found. Export from segment.html first.')
    sys.exit(1)

counts = {}
for gf in grid_files:
    print(f'\n{os.path.basename(gf)}:')
    n = process_grid(gf)
    print(f'  ✓ {n} frames extracted')
    with open(gf) as f:
        gdata = json.load(f)
    sid = infer_sheet_id(gf, gdata)
    counts[DIR_MAP.get(sid, sid)] = n

print('\n=== RESULTS ===')
for d, n in sorted(counts.items()):
    print(f'  {d}: {n}')
