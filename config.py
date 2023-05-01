import pytesseract
import os

# change this path if you would prefer a different image directory to the default
IMAGE_DIRECTORY = f"{os.getcwd()}/images"

# change this path to your Tesseract-OCR installation path
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'

# change this list if you would prefer a different hotkey combination
HOTKEY_KEYS = ["ctrl", "shift", "print screen"]