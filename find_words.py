#-*- coding=utf-8 -*-

'''
Created on 2019��3��26��

@author: Administrator
'''

import os
import re
import matplotlib.pyplot as plt
from scipy.spatial.transform import rotation
import numpy as np

with open((os.path.join('C:/Users/Administrator/Desktop','log1.txt')), 'r') as f:
    data = f.read()
    

obj = re.findall(r'(Iteration.*loss = .*)',data)
obj = ','.join(obj)
obj = obj.replace(' l','l')
obj = obj.replace(' ','=')
obj = obj.replace('===','=')
obj = obj.split(',')

##get the list of iteration
iter_list = []
for i in range(int(len(obj)/2)):
    iter_list.append(obj[2*i])


iteration = ','.join(iter_list)
iteration = iteration.replace('Iteration=', '')
iteration = iteration.split(',')
iteration = map(int, iteration)
print iteration

##get the list of loss_list
loss_list = []
for i in range(int(len(obj)/2)):
    loss_list.append(obj[2*i+1])

loss = ','.join(loss_list)
loss = loss.replace('loss=', '')
loss = loss.split(',')
loss = map(float,loss)
print type(loss)



dictionary = dict(zip(iteration,loss))

value = list(zip(iteration,loss))

plt.xticks(np.linspace(0,60000,20),rotation=45)
# plt.yticks(np.linspace(0,2,20))
plt.xlabel('Iteration')
plt.ylabel('LOSS')
plt.plot(iteration,loss)
plt.show()