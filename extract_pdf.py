from pathlib import Path
import fitz
import easyocr

pdf_path = Path('APRESENTAÇAO SMART DOG.pdf')
print('pdf exists', pdf_path.exists())
reader = easyocr.Reader(['pt'], gpu=False, verbose=False)
doc = fitz.open(pdf_path)
print('pages', len(doc))
page = doc[0]
pix = page.get_pixmap(dpi=80)
img_bytes = pix.tobytes('png')
results = reader.readtext(img_bytes, detail=0)
print('count', len(results))
for text in results[:50]:
    print(text)
