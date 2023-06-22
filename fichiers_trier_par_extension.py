"""
Trier les fichiers contenus dans le dossier data selon les associations suivantes :
mp3, wav, flac : Musique
avi, mp4, gif : Videos
bmp, png, jpg : Images
txt, pptx, csv, xls, odp, pages : Documents
autres : Divers
"""
from pathlib import Path

associations = {
    ".mp3": "Musique",
    ".wav": "Musique",
    ".flac": "Musique",
    ".avi": "Videos",
    ".mp4": "Videos",
    ".gif": "Videos",
    ".mov": "Videos",
    ".webm": "Videos",
    ".css": "Web",
    ".html": "Web",
    ".js": "Web",
    ".bmp": "Images",
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".tiff": "Images",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".ppt": "Documents",
    ".pptx": "Documents",
    ".csv": "Documents",
    ".xls": "Documents",
    ".xlsx": "Documents",
    ".odp": "Documents",
    ".pages": "Documents"
}

dossier_data = Path.cwd() / "data"
files = [f for f in dossier_data.iterdir() if f.is_file()]

for f in files:
    output_dir = dossier_data / associations.get(f.suffix, "Divers")
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)
