# encoding=utf8
# https://testpresso.swsolutions.lge.com/wp-content/Docs/testpresso/api_2.1/kr/Plugins/OCREngineTesseractPlugin/OCREngineTesseractPluginReferenceAux.html
import os
import cv2
import pytesseract


tesseract_home_path = os.environ.get('TESSERACT_HOME_PATH', r'/usr/local/Cellar/tesseract/4.1.1')
# Timeout/terminate the tesseract job after a period of time
image_url = os.path.join(os.getcwd(), "..", 'image', 'test.jpeg')
print(image_url)
rgb = cv2.imread(image_url)
image = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))  # morphology type 설정
image = cv2.morphologyEx(image, cv2.MORPH_ERODE, kernel)  # 단순화, 제거, 보정을 통해서 형태를 파악하는 목적으로 사용
_, image = cv2.threshold(image, 127, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # 이미지 임계처리

cv2.imshow('image_gray', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
decs = pytesseract.image_to_string(image, timeout=100, lang='kor')
print(decs)
# areas = pytesseract.image_to_boxes(image, timeout=100, lang='kor')
# print(areas)

