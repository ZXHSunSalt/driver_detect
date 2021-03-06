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

def get_file_path(file_name_path):
    file_paths = []
    flags = []
    files = os.listdir(file_name_path)
    for each in files:
        file_paths.append(file_name_path+'\\'+each)
        flags.append(each)
    return file_paths,flags
    

#get the name of each image and the forward filename of images
def get_img_name(file_paths,m):
    img_names = []
    imgs = os.listdir(file_paths[m])
    for img in imgs:
        img_names.append(img)
    return img_names
        
#
def write_file(file_name,store_path,items):  
    file = open(store_path+'\\'+file_name,'w')
    for item in items:
        file.write(item+'\n')
    file.close()
    
def train_new_name(file,img_names):
    new_names = []
    for img in img_names:
        new_name = file + '/' + img + ' ' + file
        new_names.append(new_name)
    return new_names

def val_new_name(file,img_names):
    new_names = []
    for img in img_names:
        new_name = img + ' ' + file
        new_names.append(new_name)
    return new_names

def main():
    file_name_path,file_name,store_path = get_items()
    file_paths ,flags = get_file_path(file_name_path)
    function = input('please input the function(train/val):')
    for i in range(len(flags)):
        img_names = get_img_name(file_paths,i)
        if function == 'train':
            new_names = train_new_name(flags[i], img_names)
        if function == 'val':
            new_names = val_new_name(flags[i], img_names)
    write_file(file_name, store_path, new_names)
    
if __name__ == '__main__':
    main()
    