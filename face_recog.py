import numpy as np
import cv2
import matplotlib.pyplot as plt
import sys, os
from PIL import Image
#%matplotlib inline

#path
in_file = "./data/shina_natsukawa/"
out_file = "./data/shina_face/"

#検出器読み込み
cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

#imagesリスト
files = os.listdir(in_file)

fileNo = 0
for i in files:
    #画像読み込み
    images = cv2.imread(in_file + i)
    #顔検出
    faces =  cascade.detectMultiScale(images, scaleFactor=1.3, minSize=(1,1))
    #認識部分を保存
    for rect in faces:
        x = rect[0]
        y = rect[1]
        width = rect[2]
        height = rect[3]
        dst = images[y:y + height, x:x + width]
        save_path = (out_file + '/' + str(fileNo) + '.jpg')
        #save
        cv2.imwrite(save_path, dst)
        plt.show(plt.imshow(np.asarray(Image.open(save_path))))
    fileNo += 1
