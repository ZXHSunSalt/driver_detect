#-*- coding=utf-8 -*-
'''
Created on 2019��3��26��

@author: Administrator
'''

import os
import sys
import numpy as np
import matplotlib.pyplot as plt

caffe_root='D:\\caffe\\caffe-master'
sys.path.insert(0,caffe_root+'python')
import caffe

plt.rcParams['figure.figsize'] = (10, 10) 
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'

caffe.set_mode_gpu()

model_def = 'D:/EclipseWorkspace/caffe_exe/train.prototxt'
model_weights = 'D:/EclipseWorkspace/caffe_exe/model/model_iter_30000.caffemodel'
net=caffe.Net(model_def, model_weights, caffe.TEST)


transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2, 0, 1))
transformer.set_raw_scale('data', 255)
transformer.set_channel_swap('data', (2, 1, 0))


image=caffe.io.load_image('D:/EclipseWorkspace/caffe_exe/val/00_06_6501_2_70b53232e9be43dfa50995b9c6678e81-h.jpg')
transformed_image = transformer.preprocess('data',image)
plt.imshow(image)





