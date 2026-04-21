from PIL import Image
import os

input_base = 'photography'
max_size = 1200
quality = 82

for root, dirs, files in os.walk(input_base):
    for filename in files:
        if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue
        filepath = os.path.join(root, filename)
        img = Image.open(filepath)
        img.thumbnail((max_size, max_size), Image.LANCZOS)
        img.save(filepath, quality=quality, optimize=True)
        print(f"Resized: {filepath}")

print("Done.")