#画像を加工して水増し

from PIL import Image, ImageFilter
import os
import numpy as np

#path
in_file = "./data/shina_face_resize/"
out_file = "./data/shina_face_padded/"


#imagesリスト
files = os.listdir(in_file)

fileNo = 0
for i in files:
    #画像読み込み
    images = Image.open(in_file + i)
    save_path = (out_file + '/' + str(fileNo) + '.jpg')
    images.save(save_path)
    fileNo += 1

    #回転とかエッジ抽出とか
    flip_LR = images.transpose(Image.FLIP_LEFT_RIGHT)
    save_path = (out_file + '/' + str(fileNo) + '.jpg')
    flip_LR.save(save_path)
    fileNo += 1

    flip_TB = images.transpose(Image.FLIP_TOP_BOTTOM)
    save_path = (out_file + '/' + str(fileNo) + '.jpg')
    flip_TB.save(save_path)
    fileNo += 1

    edge = images.filter(ImageFilter.EDGE_ENHANCE)
    save_path = (out_file + '/' + str(fileNo) + '.jpg')
    edge.save(save_path)
    fileNo += 1

    blur = images.filter(ImageFilter.BLUR)
    save_path = (out_file + '/' + str(fileNo) + '.jpg')
    blur.save(save_path)
    fileNo += 1

    for j in range(-60, 60, 4):
        rotate = images.rotate(j)
        save_path = (out_file + '/' + str(fileNo) + '.jpg')
        rotate.save(save_path)
        fileNo += 1