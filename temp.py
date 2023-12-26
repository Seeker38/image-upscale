from keras.models import Sequential
from keras.layers import Conv2D
from keras.optimizers import Adam
from skimage.metrics import structural_similarity as ssim
from matplotlib import pyplot as plt
import cv2
import numpy as np
import math
import os


#peak signal to noise ratio
def psnr(target, ref):
    #for RGB image
    target_data = target.astype(float)
    ref_data = ref.astype(float)
    differ = ref_data - target_data
    differ = differ.flatten('C')
    
    rmse = math.sqrt(np.mean(differ ** 2.))
    return 20 * math.log10(255. /rmse)

#mean squared error
def mse(target, ref):
    error = np.sum((target.astype(float) - ref.astype(float))**2 )
    error = error / float(target.shape[0] *target.shape[1])
    return error

#combine 3 image quality metrics
def compare_images(target, ref):
    compare = []
    compare.append(psnr(target, ref))
    compare.append(mse(target, ref))
    compare.append(ssim(target, ref, multichanngel = True))
    
    return compare
def degraded_images(path, factor):
    
    for file in os.listdir(path):
        
        img = cv2.imread(path + '/' + file)
        
        height, width, _ = img.shape
        new_height = height /factor
        new_width = width /factor
        
        #resize downward
        img = cv2.resize(img, (new_height, new_width), interpolation = cv2.INTER_LINEAR)
        
        #resize upward
        img = cv2.resize(img, (new_height, new_width), interpolation = cv2.INTER_LINEAR)
        #save image
        print("Saving: {}".format(file))
        cv2.imwrite('images/{}'.format(file), img)
        
degraded_images("source/", 2)