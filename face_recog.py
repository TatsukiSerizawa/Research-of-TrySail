import numpy as np
import cv2

#検出器読み込み
cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
#画像読み込み
img = cv2.imread('./data/test/momo_asakura1_1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#顔検出
faces = cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()