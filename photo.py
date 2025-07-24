# -*- coding:utf-8 -*-
# @Time     : 2021/9/24 18:08
# @Author   : 林旖睿
# @Email    : 473429801@qq.com
# @File     : photo.py
# @Software : PyCharm

#代码旨在修改图片大小
# -*- coding: utf-8 -*-
import os
import glob
from PIL import Image
import os.path



#'''修改图片文件大小jpgfile：图片文件；savedir：修改后要保存的路径'''

def convertjpg(jpgfile, savedir, width=580, height=550):
    img = Image.open(jpgfile)
    new_img = img.resize((width, height), Image.BILINEAR)
    new_img.save(os.path.join(savedir, os.path.basename(jpgfile)))

#'''查找给定路径下图片文件，并修改其大小'''

def modifyjpgSize(file, saveDir):
    for jpgfile in glob.glob(file):
        convertjpg(jpgfile, saveDir)

# 测试代码
file = r'C:\\Users\\林旖睿\\Desktop\\相册\\img\\*.jpg'
saveDir = r'C:\\Users\\林旖睿\\Desktop\\相册\\img'
modifyjpgSize(file, saveDir)