# coding=utf-8  
from PIL import Image  
import shutil  
import os  
import cv2

class Graphics:  
    '''图片处理类
    
    参数: infile, outfile
    ------
    infile: 加载图片文件的路径
    outfile: 转存图片文件的路径
    '''
    def __init__(self, infile, outfile):
        self.infile = infile
        self.outfile = outfile
  
    def cut_by_ratio(self):  
        """按照图片长宽进行分割
        
        参数: None
        ------
        取中间的部分，裁剪成正方形
        """  
        im = Image.open(self.infile)  
        (x, y) = im.size
        print (x,y)
        m = int(x/4)
        n = int(y/4)
#         if x > y:  
#             for i in range(2):
#                 region = (0+i*m, 0, int((3/4)*x)+m*i, int((5/6)*y))  
#                  #裁切图片  
#                 crop_img = im.crop(region)
#                  #保存裁切后的图片      
#                 crop_img.save(self.outfile)      
#         elif x < y:  
#         	for i in range(2):
# 	            region = (0, 0+i*n, x, int((3/4)*y)+i*n)
# 	            #裁切图片  
# 	            crop_img = im.crop(region)  
# 	            #保存裁切后的图片  
# 	            crop_img.save(self.outfile)
        if x > y:  
            region = (m,n,4*m,4*n)  
            #裁切图片  
            crop_img = im.crop(region)  
            #保存裁切后的图片  
            crop_img.save(self.outfile)             
        elif x < y:  
            region = (0, int(y/2-x/2), x, int(y/2+x/2))
            #裁切图片  
            crop_img = im.crop(region)  
            #保存裁切后的图片  
            crop_img.save(self.outfile)