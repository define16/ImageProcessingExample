import os

import cv2, sys
from matplotlib import pyplot as plt
import numpy as np

image_url = os.path.join(os.getcwd(), 'image', 'test.jpg')

image = cv2.imread(image_url)
image_gray = cv2.imread(image_url, cv2.IMREAD_GRAYSCALE)

cv2.imshow('image', image)
cv2.imshow('image_gray', image_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
