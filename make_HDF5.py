# -*- coding:utf-8 -*-
'''
Created on 2018年11月13日

@author: Lenovo
'''
import re
import h5py
import numpy as np
import os
import math
import cv2
import random

##import various models
root_path = 'E:\\Eclipse workspace\\caffe_exe\\hdf5\\hdf5_image'

with open('E:\\Eclipse workspace\\caffe_exe\\hdf5\\hdf5.txt','r') as f:
    lines = f.readlines()
print(lines)

##define the path of images and read image feature txt files and shuffle these data
num = len(lines)       #count the number of images
random.shuffle(lines)  #disrupting the original order    

##using openCV read data and process data
#define imgAcc\imgs\labels
imgAcc = 0
imgs = np.zeros([num,3,224,224])
labels = np.zeros([num,10])
#read image data and do mean process on label according the images
for i in range(num):
    line = lines[i]
    segments = re.split('\s+', line)
    img = cv2.imread(os.path.join(root_path,segments[0]))#according the path reading the image
    img = cv2.resize(img,(224,224))                      #resize the image
    img = img.transpose(2,0,1)                           #transform c-h-w to h-w-c
    imgs[i,:,:,:] =img.astype(np.float32)
    for j in range(10):
        labels[i,j] = float(segments[j+1])*244/256  
        
##do some preprocessing in images and labels like minus the mean value
#define batchsize and batchNum
batchsize = 1
batchNum = int(math.ceil(1.0*num/batchsize))
#de mean process on images and label
imgsMean = np.mean(imgs,axis=0) 
#imgs = (imgs - imgsMean)/255.0
labelsMean = np.mean(labels, axis=0)
labels = (labels - labelsMean)/10

##using os model to creat the txt file to store the path of hf file
#judge wheather the txt file is existed
if os.path.exists('trainlist.txt'):
    os.remove('trainlist.txt')
if os.path.exists('testlist.txt'):
    os.remove('testlist.txt')
#crate txt file
comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}
for i in range(batchNum):
    start = i*batchsize
    end = min(num,(i+1)*batchsize)
    if i < (batchNum-1):    #according IF judge statement to define the number of train set and test set
        #filename = 'E:\\Eclipse workspace\\caffe_exe\\hdf5\\train{0}.h5'.format(i)
        filename = 'E:\\Eclipse workspace\\caffe_exe\\hdf5\\train{0}.h5'.format(i,i+1)
    else:
        filename = 'E:\\Eclipse workspace\\caffe_exe\\hdf5\\test{0}.h5'.format(i-batchNum+1)
    #crate the hdf5 file
    with h5py.File(filename,'w') as f:
        f.create_dataset('data',data = np.array((imgs[start:end]-imgsMean)/255).astype(np.float32),**comp_kwargs)
        f.create_dataset('label',data = np.array(labels[start:end]).astype(np.float32),**comp_kwargs)

    if i < (batchNum-1):
        with open('E:\\Eclipse workspace\\caffe_exe\\hdf5\\trainlist.txt', 'a') as f:
            f.write(os.path.join('E:\\Eclipse workspace\\caffe_exe\\hdf5','train{0}.h5').format(i) + '\n')
    else:
        with open('E:\\Eclipse workspace\\caffe_exe\\hdf5\\testlist.txt', 'a') as f:
            f.write(os.path.join('E:\\Eclipse workspace\\caffe_exe\\hdf5','test{0}.h5').format(i-batchNum+1) + '\n')

imgsMean = np.mean(imgsMean, axis=(1,2))
with open('mean.txt', 'w') as f:
    f.write(str(imgsMean[0]) + '\n' + str(imgsMean[1]) + '\n' + str(imgsMean[2]))
    



