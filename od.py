import cv2 as opencv
import numpy as np
from cca import neighbours


def opticDisc(imgout, labelsMat, map, original, fname):  # img is cca image
    counts = [0] * len(labelsMat)
    for j in range(imgout.shape[0]):
        for k in range(imgout.shape[1]):
            x = imgout[j, k]
            if x != 0:
                pos = labelsMat.index(x)
                if map[j, k] == 255:
                    counts[pos] += 1

    maxc = max(counts)
    ind = counts.index(maxc)
    maxl = labelsMat[ind]
    for i in range(imgout.shape[0]):
        for j in range(imgout.shape[1]):
            if imgout[i, j] == maxl:
                imgout[i, j] = 255
            else:
                imgout[i, j] = 0

    M = opencv.moments(imgout)
    # calculate x,y coordinate of center
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    i = cX
    j = cY

    Xradius = 1

    while True:
        if np.count_nonzero(neighbours(j, cX, imgout)) < 2:
            break
        else:
            Xradius = Xradius + 1
            j += 1
    Yradius = 1
    while True:
        if np.count_nonzero(neighbours(cY, i, imgout)) < 2:
            break
        else:
            Yradius = Yradius + 1
            i += 1

    radius = max(Xradius, Yradius)
    original = opencv.circle(original, (cX, cY), radius, 190, 2)
    #opencv.imwrite('images/output/'+fname + '.JPG', original)
    opencv.namedWindow('Optic Disc Labelled', opencv.WINDOW_NORMAL)
    opencv.imshow('Optic Disc Labelled', original)

    imgout = opencv.circle(imgout, (cX, cY), radius, 190, 2)
    #opencv.imwrite('images/binary/' + fname + '.JPG', imgout)
    opencv.namedWindow('Binary Optic Disc labelled', opencv.WINDOW_NORMAL)
    opencv.imshow('Binary Optic Disc labelled', imgout)
    return cX, cY
