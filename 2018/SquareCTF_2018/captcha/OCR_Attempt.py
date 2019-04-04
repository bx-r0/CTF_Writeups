import numexpr as nx
import pytesseract
import cv2
import sys

if len(sys.argv) == 2:
    img_path = sys.argv[1]
else:
    print("[*] Usage: python OCR_Attempt IMAGE_PATH")
    exit()

# Read image from disk
im = cv2.imread(img_path, cv2.IMREAD_REDUCED_GRAYSCALE_2)
scale_percentage = 100

# Resizing
width = int(im.shape[1] * scale_percentage / 100)
height = int(im.shape[0] * scale_percentage / 100)
dim = (width, height)
im_resize = cv2.resize(im, dim, interpolation=cv2.INTER_AREA)

# Run tesseract OCR on image
text = pytesseract.image_to_string(image=im_resize, lang="eng")

print(text)
