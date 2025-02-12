from os.path import join

import matplotlib.pyplot as plt

from util.img_util import readImageFile, saveImageFile, ImageDataLoader
from util.inpaint_util import removeHair

data_dir = "./data"
save_dir = './result'

lower_bound = 1703
upper_bound = 1902
i = lower_bound

# read all image files in data_dir, remove hair and save the result
for img_rgb, img_gray in ImageDataLoader(data_dir, bounds=[lower_bound,upper_bound]):
    _, _, img_out = removeHair(img_rgb, img_gray)
    save_file_path = join(save_dir, 'output%04d.jpg' % i)
    saveImageFile(img_out, save_file_path)
    i+= 1
    

