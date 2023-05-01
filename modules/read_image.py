from modules.popup import create_popup
import pytesseract

def read_image(image):
    image_Text = pytesseract.image_to_string(image)
    create_popup(image_Text)
