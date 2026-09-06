from pathlib import Path
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "tmp" / "qa-gal-glossary-final"
OUTPUT = ROOT / "output" / "pdf" / "מילון-המושגים-החדשים-של-גל-קריא-בכל-מכשיר.pdf"


def page_number(path: Path) -> int:
    return int(path.stem.split("-")[-1])


pages = sorted(SOURCE_DIR.glob("page-*.png"), key=page_number)
if not pages:
    raise FileNotFoundError(f"No rendered pages found in {SOURCE_DIR}")

images = []
try:
    for page in pages:
        with Image.open(page) as image:
            images.append(image.convert("RGB"))

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    images[0].save(
        OUTPUT,
        "PDF",
        save_all=True,
        append_images=images[1:],
        resolution=180.0,
        quality=95,
        optimize=True,
    )
finally:
    for image in images:
        image.close()

print(OUTPUT)
