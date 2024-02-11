import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# load image, grayscale, apply sharpening filter, otsu's threshold 
image = cv2.imread('meter.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpen = cv2.filter2D(gray, -1, sharpen_kernel)
thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# ocr
data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 6')

# cv2.imshow('sharpen', sharpen)
# cv2.imshow('thresh', thresh)
# cv2.waitKey()
numbers = ''.join(filter(str.isdigit, data))

# Print extracted numbers
print("Extracted Numbers:", numbers)
