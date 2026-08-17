import shutil
from pathlib import Path

import kagglehub

cache_path = kagglehub.dataset_download("austinreese/craigslist-carstrucks-data")
print("kagglehub cache path:", cache_path)

archive_dir = Path("archive")
archive_dir.mkdir(exist_ok=True)

for source_file in Path(cache_path).iterdir():
    destination_file = archive_dir / source_file.name
    shutil.copy2(source_file, destination_file)
    size_mb = destination_file.stat().st_size / (1024 * 1024)
    print(f"Copied {source_file.name} -> archive/  ({size_mb:.2f} MB)")
