#-*- coding=utf-8 -*-
'''
Created on 2019.3.22

@author: Administrator
'''
import cv2
import os 

def get_items():
    file_path = input('please input the file path:')
    store_path = input('please input the store path:')  
    return file_path,store_path

def get_file_name(file_name_path):
    img_names = []
    #get the each file name in train 
    files = os.listdir(file_name_path)
    return files
# def get_img_name(file_path):
#     img_names = []
#     files = get_file_name(file_path)
#     #get each image name in each file
#     imgs = os.listdir(file_path + '/' + file)
#     for img in imgs:
#         img_names.append(img)
        
def img_resize():
    file_path,store_path=get_items()
    files = get_file_name(file_path)
    for file in files:
        imgs = os.listdir(file_path + '/' + file)
        for each in imgs:
            img = cv2.imread(file_path + '/' + file + '/' + each)
            new_img = cv2.resize(img,(128,128),interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(store_path + '/' + file+ '/' + each , new_img)
    

if __name__ == '__main__':
    img_resize()