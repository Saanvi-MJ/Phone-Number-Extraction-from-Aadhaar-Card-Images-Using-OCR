import cv2
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_phone_number(image_path):
    img = cv2.imread(image_path)

    
    if img is None:
        return "Error: Unable to load the image. Check the file path or format."

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)

    phone_pattern = r'\b[6-9]\d{9}\b'
    phone_numbers = re.findall(phone_pattern, text)

    if phone_numbers:
        return phone_numbers
    else:
        return "No phone number found in the image."

image_path = r"Aadhaar card.jpeg"
phone_numbers = extract_phone_number(image_path)
print("Extracted Phone Numbers:", phone_numbers)
