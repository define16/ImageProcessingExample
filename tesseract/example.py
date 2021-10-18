# encoding=utf8
# https://testpresso.swsolutions.lge.com/wp-content/Docs/testpresso/api_2.1/kr/Plugins/OCREngineTesseractPlugin/OCREngineTesseractPluginReferenceAux.html
import os
tesseract_home_path = os.environ.get('TESSERACT_PATH', r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract')
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = tesseract_home_path

# Simple image to string

# List of available languages
tessdata_dir_config = "/usr/local/Cellar/tesseract/4.1.1"
print(pytesseract.get_languages(config=''))

# French text image to string
# print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))

# In order to bypass the image conversions of pytesseract, just use relative or absolute image path
# NOTE: In this case you should provide tesseract supported images or tesseract will return error
print(pytesseract.image_to_string('test.png'))

# Batch processing with a single file containing the list of multiple image file paths
print(pytesseract.image_to_string('images.txt'))

# Timeout/terminate the tesseract job after a period of time
try:
    print(pytesseract.image_to_string('test.jpg', timeout=2))  # Timeout after 2 seconds
    print(pytesseract.image_to_string('test.jpg', timeout=0.5))  # Timeout after half a second
except RuntimeError as timeout_error:
    # Tesseract processing is terminated
    pass

# Get bounding box estimates
print(pytesseract.image_to_boxes(Image.open('test.png')))

# Get verbose data including boxes, confidences, line and page numbers
print(pytesseract.image_to_data(Image.open('test.png')))

# Get information about orientation and script detection
print(pytesseract.image_to_osd(Image.open('test.png')))

# Get a searchable PDF
pdf = pytesseract.image_to_pdf_or_hocr('test.png', extension='pdf')
with open('test.pdf', 'w+b') as f:
    f.write(pdf) # pdf type is bytes by default

# Get HOCR output
hocr = pytesseract.image_to_pdf_or_hocr('test.png', extension='hocr')

# Get ALTO XML output
xml = pytesseract.image_to_alto_xml('test.png')