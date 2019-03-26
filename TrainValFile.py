#-*- coding=utf-8 -*-
'''
Created on 2019年3月22日

@author: Administrator
'''
import os 


#获取相应的待处理图片路径，文件名，保存路径
#get the 
def get_items():
    file_name_path = input('please input the file path:')
    file_name = input('please input the file name:')
    store_path = input('please input the txt store path:')  
    return file_name_path,file_name,store_path


#get the name of each image and the forward filename of images
def get_file_name(file_name_path):
    img_names = []
    #get the each file name in train 
    files = os.listdir(file_name_path)
    for each in files:
        #get each image name in each file
        imgs = os.listdir(file_name_path + '\\' + each)
        for img in imgs:
            img_names.append(img)
    return img_names,files
        
#
def write_file(file_name,store_path,items):  
    file = open(store_path+'\\'+file_name,'w')
    for item in items:
        file.write(item+'\n')
    file.close()
    
def train_new_name(files,img_names):
    new_names = []
    for each in files:
        for img in img_names:
            new_name = each + '/' + img + ' ' + each
            new_names.append(new_name)
    return new_names

def val_new_name(files,img_names):
    new_names = []
    for each in files:
        for img in img_names:
            new_name = img + ' ' + each
            new_names.append(new_name)
    return new_names

def main():
    file_name_path,file_name,store_path = get_items()
    img_names , files = get_file_name(file_name_path)
    function = input('please input the function(train/val):')
    if function == 'train':
        new_names = train_new_name(files, img_names)
    if function == 'val':
        new_names = val_new_name(files, img_names)
    write_file(file_name, store_path, new_names)
    
if __name__ == '__main__':
    main()
    