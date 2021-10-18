# encoding=utf8
# https://testpresso.swsolutions.lge.com/wp-content/Docs/testpresso/api_2.1/kr/Plugins/OCREngineTesseractPlugin/OCREngineTesseractPluginReferenceAux.html
import os
import cv2
import pytesseract

tesseract_home_path = os.environ.get('TESSERACT_HOME_PATH', r'/usr/local/Cellar/tesseract/4.1.1')
# Timeout/terminate the tesseract job after a period of time
image_url = os.path.join(os.getcwd(), 'image', 'test.jpg')
print(image_url)
image = cv2.imread(image_url)
decs = pytesseract.image_to_string(image, timeout=100, lang='kor')
print(decs)
