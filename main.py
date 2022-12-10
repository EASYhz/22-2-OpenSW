"""
!pip install -r requirements.txt
"""

import pytesseract
import cv2
import os
from PIL import Image

# Image
image = cv2.imread('img.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Read file in os
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# lang : Language to use
text = pytesseract.image_to_string(Image.open(filename), lang=None)
os.remove(filename)

# Show result
print(text)
# cv2.imshow('image', image)

# 함수
# 1. 숫자, 기호 판별 ? .. 그냥 수식 이미지만 넣을 것인가
# 2. 계산
# 3. 결과

