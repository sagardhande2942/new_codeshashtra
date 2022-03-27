import cv2
import numpy as np
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# img3 = cv2.imread('image.jpg')   #any picture

def mfun(path):
    img3 = cv2.imread(path)
    print(img3.shape)

    # removing shadow/noise from image which can be taken from phone camera

    rgb_planes = cv2.split(img3)
    result_planes = []
    result_norm_planes = []
    for plane in rgb_planes:
        dilated_img = cv2.dilate(plane, np.ones((10, 10), np.uint8))        #change the value of (10,10) to see different results
        bg_img = cv2.medianBlur(dilated_img, 21)
        diff_img = 255 - cv2.absdiff(plane, bg_img)
        norm_img = cv2.normalize(diff_img, None, alpha=0, beta=250, norm_type=cv2.NORM_MINMAX,
                                                    dtype=cv2.CV_8UC1)
        result_planes.append(diff_img)
        result_norm_planes.append(norm_img)

    result = cv2.merge(result_planes)
    result_norm = cv2.merge(result_norm_planes)
    dst = cv2.fastNlMeansDenoisingColored(result_norm, None, 10, 10, 7, 11)             # removing noise from image

    text = pytesseract.image_to_string(dst).upper().replace(" ", "")

    date = str(re.findall(r"[\d]{1,4}[/-][\d]{1,4}[/-][\d]{1,4}", text)).replace("]", "").replace("[","").replace("'", "")
    output  = []
    print(date)
    output.append(date)
    number = str(re.findall(r"[0-9]{11,12}", text)).replace("]", "").replace("[","").replace("'", "")
    print(number)
    output.append(number)
    sex = str(re.findall(r"MALE|FEMALE", text)).replace("[","").replace("'", "").replace("]", "")
    output.append(sex)
    print(sex)

    # cv2.imshow('original',img3)
    # cv2.imshow('edited',dst)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


    # crop_pic from ID card

    # gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
    # face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "construct_user/haarcascade_frontalface_default.xml")
    # faces = face_cascade.detectMultiScale(gray, 1.3, 7)
    # for (x, y, w, h) in faces:
    #     ix = 0
    #     cv2.rectangle(img3, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #     roi_color = img3[y:y + h, x:x + w]
    #     #crop_pic = cv2.imwrite('croppic10.jpg', roi_color)
    #     crop_pic = cv2.imshow('croppicds', roi_color)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()

    return output
