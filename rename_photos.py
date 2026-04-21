import os

# Map each folder path to the prefix you want for filenames
folders = {
    'photography/north-america/ontario': 'ontario',
    'photography/north-america/kelowna': 'kelowna',
    'photography/north-america/florida': 'florida',
    'photography/north-america/dominican-republic': 'dr',
    'photography/ireland': 'dublin',
    'photography/europe/netherlands': 'amsterdam',
    'photography/europe/denmark': 'copenhagen',
    'photography/europe/sweden': 'stockholm',
    'photography/europe/uk': 'uk',
    'photography/europe/germany': 'germany',
    'photography/europe/spain': 'spain',
    'photography/europe/france': 'france',
    'photography/europe/portugal': 'portugal',
    'photography/italy': 'italy',
    'photography/morocco': 'morocco',
}

for folder_path, prefix in folders.items():
    if not os.path.exists(folder_path):
        print(f"Skipping {folder_path} - folder not found")
        continue
    
    files = sorted([
        f for f in os.listdir(folder_path)
        if f.lower().endswith(('.jpg', '.jpeg', '.png'))
    ])
    
    for i, filename in enumerate(files, start=1):
        ext = os.path.splitext(filename)[1].lower()
        new_name = f"{prefix}-{i}{ext}"
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_name}")

print("\nDone.")