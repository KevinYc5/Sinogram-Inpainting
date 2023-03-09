######### 将training(testing)_image_data 中 .IMA 格式数据转换为 .png 和 .npy #############

import pydicom
import matplotlib.pyplot as plt
import numpy as np
import cv2
import torch
from PIL import Image
import os
from tqdm import tqdm

def get_files(path):
    for filepath,dirnames,filenames in tqdm(os.walk(path+'/full_1mm/')):
        for filename in filenames:
            filePath = os.path.join(filepath,filename)
            img = pydicom.read_file(filePath)
            img = img.pixel_array
            # print(img.shape)  #512*512
            # print("img", img.max().item(), img.min().item(), img.dtype)
            # np.save('Data/num_512/'+f'{str(filename)}.npy', img)
            plt.imsave('Data/image_512/'+f'{str(filename)}.png', img, cmap='gray')

						#改变图片尺寸 512->256
            # img2 = cv2.resize(img, dsize=(256, 256), interpolation=cv2.INTER_CUBIC)
            # img2 = img2/1.0                    #float64
            # print(img2.shape)                  #(256, 256)
            # img2 = np.float32(img2)            #float32
            # np.save('Data/num_256/'+f'{str(filename)}.npy', img2)
            # plt.imsave('Data/image_256/'+f'{str(filename)}.png', img2, cmap='gray')

if __name__ == '__main__':
    path = 'Data/full_1mm'
    paths = os.listdir(path)
    for p in paths:
        p = os.path.join(path, p)
        print("p: ", p)
        get_files(p)