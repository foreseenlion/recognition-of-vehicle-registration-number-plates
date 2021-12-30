#pip3 install easyocr
#pip3 install imutils
import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
import easyocr

#Reading image
IMAGE_PATH = cv2.imread('english_1.jpg')

#Extracting text from the image
reader = easyocr.Reader(['en'])
result = reader.readtext(IMAGE_PATH,paragraph="False")
print(result)

#Draw results for multiple lines
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.imread('english_1.jpg')
spacer = 100
for detection in result: 
    top_left = tuple(detection[0][0])
    bottom_right = tuple(detection[0][2])
    text = detection[1]
    img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),3)
    img = cv2.putText(img,text,(20,spacer), font, 0.5,(0,255,0),2,cv2.LINE_AA)
    spacer+=15
plt.figure(figsize=(10,10))
plt.imshow(img)
plt.show()
