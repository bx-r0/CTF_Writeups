import cv2 as cv2
import pytesseract
import sys  

def resize(im, scale_percentage):
    width = int(im.shape[1] * scale_percentage / 100)
    height = int(im.shape[0] * scale_percentage / 100)
    dim = (width, height)
    return cv2.resize(im, dim, interpolation=cv2.INTER_AREA)

def crop(im, x, y):
    w = 350
    h = 75
    return im[y:y+h, x:x+w]

# How many frames are skipped in one go
FRAME_SKIP = 25

# Built in openCV variables
CV_CAP_PROP_POS_FRAMES = 1
CV_CAP_PROP_FRAME_COUNT = 7

success = True
video = cv2.VideoCapture("./training.mp4")
total_frames = video.get(CV_CAP_PROP_FRAME_COUNT)

frame_val = 1059675

while success:

    video.set(CV_CAP_PROP_POS_FRAMES, frame_val)

    # Frame read
    (success, frame) = video.read()

    # Skips a number of frames
    frame_val += FRAME_SKIP
    
    # Crops the bottom of the frame, this is where the flag will appear
    crop_img = crop(frame, x=0, y=150)
    # crop_img = resize(crop_img, 200)

    # OCR method
    text = pytesseract.image_to_string(image=crop_img, lang="eng")

    if "FLAG" in text:
        sys.stdout.write("TEXT: ")
        sys.stdout.write(text)
        sys.stdout.write("\n")
        cv2.imwrite(f"FLAG_{frame_val}.png", crop_img)

    # # Code used to show the images
    # cv2.imshow("normal", frame)
    # cv2.imshow("cropped", crop_img)
    # cv2.waitKey(0)

    sys.stderr.write(f"PROGRESS: {round(frame_val / total_frames * 100, 2)}%\r")


