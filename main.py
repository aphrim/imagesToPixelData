import numpy as np
import cv2 as cv
import math
import os
from random import randint
from PIL import Image
import time
print('Gathering Frames')
frames = [[]]
frameDirectory = r'C:\Code\ImageUploader\frames'
fileList = os.listdir(frameDirectory)



finalOutput = ''
p = 0
outputFile = open(r'output.txt', 'a')

frames = []
frameDirectory = frameDirectory
filesUnsorted = os.listdir(frameDirectory)
fileList = []

lastPixels = [] * 21000

for entry in (filesUnsorted):

    image = cv.imread('frames\\' + entry)

    pixels = [] * 21000
    basewidth = 300
    outputFile.write('\n v[' + str(p) + '] = {} \n')
    for i in range(20736) :
        pixel = image[i%144,math.floor(i/144)]
        hexCode = '#%02x%02x%02x' % (pixel[2], pixel[1], pixel[0])
        if (len(lastPixels) < 20736):
            lastPixels.append(hexCode)
        if (hexCode != lastPixels[i]):
            pixels.insert(i, hexCode)
            lastPixels.insert(i, hexCode)
            outputFile.write(' v[' + str(p) + '][' + str(i) + '] = "' + hexCode + '"  ')  

    if(randint(0,10) == 10):
        outputFile.write('Task.Wait(0.1) \n')    
    p += 1  
outputFile.close()