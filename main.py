from os.path import join

import matplotlib.pyplot as plt

from util.img_util import readImageFile, saveImageFile, ImageDataLoader
from util.inpaint_util import removeHair

data_dir = "./data"
save_dir = './result'

i=1703

# read all image files in data_dir, remove hair and save the result
for img_rgb, img_gray in ImageDataLoader(data_dir):
    _, _, img_out = removeHair(img_rgb, img_gray)
    save_file_path = join(save_dir, 'output%04d.jpg' % i)
    saveImageFile(img_out, save_file_path)
    i+= 1

