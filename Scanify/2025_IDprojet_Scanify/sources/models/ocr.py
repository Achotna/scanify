#Projet : Scanify
#Auteurs : Antonina Savchenko, Elisa Salignon

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
        #Ajoutez votre chemin vers tesseract.exe ici
        window_path=r"tesseract_download\tesseract.exe"
        pytesseract.tesseract_cmd=window_path

    def extract_text(self, image: str, lang: str) -> str:
        img=Image.open(image)
        extracted_text=pytesseract.image_to_string(img, lang=lang)
        return extracted_text
    

