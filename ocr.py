import pytesseract
import cv2

img = cv2.imread('test.png')

custom_config = r'--oem 3 --psm 6 outputbase digits'
print(pytesseract.image_to_string(img, config=custom_config))

cv2.imshow("img", img)
cv2.waitKey(0)

# import cv2
# import pytesseract

# img = cv2.imread('test.png')

# h, w, c = img.shape
# boxes = pytesseract.image_to_boxes(img)
# for b in boxes.splitlines():
# b = b.split(' ')
# img = cv2.rectangle(img, (int(b[1]), h - int(b[2])),
# (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

# cv2.imshow('img', img)
# cv2.waitKey(0)

# import re
# import cv2
# import pytesseract
# from pytesseract import Output

# img = cv2.imread(r"test.jpeg")
# d = pytesseract.image_to_data(img, output_type=Output.DICT)
# keys = list(d.keys())

# date_pattern = '^[0-9]*$'

# n_boxes = len(d['text'])
# for i in range(n_boxes):
# if int(d['conf'][i]) > 60:
# if re.match(date_pattern, d['text'][i]):
# (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i],
# d['height'][i])
# img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# cv2.imshow('img', img)
# cv2.waitKey(0)
