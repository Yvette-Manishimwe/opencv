# Import necessary libraries
import cv2  # OpenCV library for computer vision tasks
import numpy as np  # NumPy library for numerical operations
import pytesseract  # Tesseract OCR library for text extraction from images

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Read the image using OpenCV
image = cv2.imread('meter.png')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define a sharpening kernel for image enhancement
sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])

# Apply the sharpening kernel to the grayscale image
sharpen = cv2.filter2D(gray, -1, sharpen_kernel)

# Apply Otsu's thresholding to create a binary image
thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Perform OCR on the thresholded image to extract text
data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 6')

# Extract only numeric characters from the OCR result
nums = ''.join(filter(str.isdigit, data))

# Print the extracted numeric characters
print("Extracted numbers:", nums)

