import sys
from PIL import Image, ImageDraw
# usage: montage.py out.jpg cols "label|path" ...
out, cols = sys.argv[1], int(sys.argv[2]); items = [a.split("|", 1) for a in sys.argv[3:]]
W, H, L = 480, 270, 22
rows = (len(items) + cols - 1) // cols
sheet = Image.new("RGB", (cols * W, rows * (H + L)), "white"); d = ImageDraw.Draw(sheet)
for i, (lab, p) in enumerate(items):
    im = Image.open(p).convert("RGB").resize((W, H))
    x, y = (i % cols) * W, (i // cols) * (H + L)
    sheet.paste(im, (x, y + L)); d.text((x + 4, y + 4), lab[:70], fill="black")
sheet.save(out, quality=85)
