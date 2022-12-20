import numpy as np
import cv2 as opencv
import Transforms
import od as o
import cca
import pad as p
import csv
import os


def transforms(img):
    output = Transforms.ContrastStretching(img, 97, 100)
    for i in range(5):
        output = Transforms.maxFilter(output, 3)
    return output


def applyCCA(img):
    output = p.gray2binary(img, 90)
    opencv.namedWindow('Transformed output', opencv.WINDOW_NORMAL)
    opencv.imshow('Transformed output', output.astype("uint8"))
    opencv.waitKey(0)
    output = p.padArray(output, 1)
    c, output = cca.connectedComponentAnalysis(output, 255, 1)
    colored = cca.colorObjects(output)
    return output, colored


def getOpticDisc(output, rgb, map, fname):  # output of CCA is fed into this function to get optic disc
    labels = np.unique(output)
    labels = labels.tolist()
    nervesmap = map
    nervesmap = p.gray2binary(nervesmap, 127)
    x, y = o.opticDisc(output, labels, nervesmap, rgb, fname)
    return x, y


#f = open('record.csv', 'w', newline='')
#writer = csv.writer(f)
rgbimage, grayimage, mapimage = 0, 0, 0
#for (fundus, map_fundus) in zip(os.listdir('images/fundus'), os.listdir('images/vessels')):
#    if fundus.endswith('.jpg') or fundus.endswith('.jpeg') or fundus.endswith('.png') or fundus.endswith(
#            '.tif') or fundus.endswith('.JPG'):
#        rgbimage = opencv.imread('images/fundus/' + fundus)
#        rgbimage = opencv.resize(rgbimage, [500, 500])
#        grayimage = opencv.imread('images/fundus/' + fundus, opencv.IMREAD_GRAYSCALE)
#        grayimage = opencv.resize(grayimage, [500, 500])

#    if map_fundus.endswith('.jpg') or map_fundus.endswith('.jpeg') or map_fundus.endswith(
#            '.png') or map_fundus.endswith(
#            '.tif') or map_fundus.endswith('.JPG'):
#        mapimage = opencv.imread('images/vessels/' + map_fundus, opencv.IMREAD_GRAYSCALE)
#        mapimage = opencv.resize(mapimage, [500, 500])



rgbimage = opencv.imread('1ffa92e4-8d87-11e8-9daf-6045cb817f5b..JPG')
mapimage = opencv.imread('1ffa952f-8d87-11e8-9daf-6045cb817f5b._bin_seg.png', opencv.IMREAD_GRAYSCALE)
grayimage = opencv.imread('1ffa92e4-8d87-11e8-9daf-6045cb817f5b..JPG', opencv.IMREAD_GRAYSCALE)
rgbimage = opencv.resize(rgbimage, [500, 500])
grayimage = opencv.resize(grayimage, [500, 500])
mapimage = opencv.resize(mapimage, [500, 500])

t_out = transforms(grayimage)
#opencv.imwrite('images/transformed/'+ fundus+'.JPG', t_out)
cca_out, colored = applyCCA(t_out)
#opencv.imwrite('images/ccaoutput/' + fundus + '.JPG', colored)
#fname = fundus
fname ='ali'
x, y = getOpticDisc(cca_out, rgbimage, mapimage, fname)
center = (x, y)
#writer.writerow(center)
opencv.waitKey(0)

#f.close()
