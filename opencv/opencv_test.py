import os
## https://opencv-python.readthedocs.io/en/latest/index.html
import cv2
from matplotlib import pyplot as plt
import numpy as np

image_url = os.path.join(os.getcwd(), '..', 'image', 'test.jpg')
print(image_url)

large = cv2.imread(image_url)
rgb = cv2.pyrDown(large)  # 이미지 피라미드, 50%로 이미지를 작게 만든다.
small = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))  # morphology type 설정
grad = cv2.morphologyEx(small, cv2.MORPH_GRADIENT, kernel)  # 단순화, 제거, 보정을 통해서 형태를 파악하는 목적으로 사용
_, bw = cv2.threshold(grad, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # 이미지 임계처리
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 1))
connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)
# # using RETR_EXTERNAL instead of RETR_CCOMP
contours, hierarchy = cv2.findContours(connected.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # 윤곽 검출
mask = np.zeros(bw.shape, dtype=np.uint8)
word_area = []

for idx in range(len(contours)):
    x, y, w, h = cv2.boundingRect(contours[idx])
    mask[y:y+h, x:x+w] = 0
    word_area.append(((x, x+w), (y, y+h)))
    cv2.drawContours(mask, contours, idx, (255, 255, 255), -1)
    r = float(cv2.countNonZero(mask[y:y+h, x:x+w])) / (w * h)
    if r > 0.45 and w > 8 and h > 8:
        cv2.rectangle(rgb, (x, y), (x+w-1, y+h-1), (0, 255, 0), 2)
        # word_area.append(((x, y), (x+w-1, y+h-1)))

idx = 0
# 글자만 이미지 추출
for x, y in word_area:
    img = rgb[y[0]:y[1], x[0]:x[1]]
    print(img)
    cv2.imshow(f'img_{idx}', img)
    cv2.waitKey()

# show image with contours rect
cv2.imshow('rects', rgb)
cv2.waitKey()
print(word_area)


