from PIL import Image
from pytesseract import pytesseract
import enum

class Language(enum.Enum):
    EN = 'eng'
    RUS = 'rus'
    ITA = 'ita'
    FR = 'fra'

class ImageReader:

    def __init__(self):
        window_path=r"C:\Users\Eleve\Desktop\Lycée\Première\NSI\Myapp\tess\4\tesseract.exe"
        pytesseract.tesseract_cmd=window_path

    def extract_text(self, image: str, lang: str) -> str:
        img=Image.open(image)
        extracted_text=pytesseract.image_to_string(img, lang=lang)
        return extracted_text
    

