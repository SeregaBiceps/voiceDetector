import time
import numpy as np
import pyscreenshot as ImageGrab
import cv2
import os
import pytesseract

filename = 'Image.png'
x1 = 1633
y1 = 282
x2 = 1920
y2 = 1080
screen = np.array(ImageGrab.grab(bbox=(x1, y1, x2, y2)))
cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
cv2.imwrite(filename, screen)
cv2.destroyAllWindows()
img = cv2.imread('Image.png')
text = pytesseract.image_to_string(img)
boxes = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
result = []
cnt = 0
for i in range(len(boxes['text'])):
	try:
		if 'CS' in boxes['text'][i]:
			cnt += 1
			result.append({cnt: [boxes['left'][i], boxes['top'][i]]})
	except:
		continue
print(result)