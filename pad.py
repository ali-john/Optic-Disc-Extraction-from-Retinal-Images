import numpy as np


def padArray(inputImg, size):
    pad_arr = np.zeros([inputImg.shape[0] + size * 2, inputImg.shape[1] + size * 2], dtype="uint8")
    for i in range(size, inputImg.shape[0] - size):
        for j in range(size, inputImg.shape[1] - size):
            pad_arr[i, j] = inputImg[i, j]
    return pad_arr


def gray2binary(inputImg, threshold):
    for i in range(inputImg.shape[0]):
        for j in range(inputImg.shape[1]):
            if inputImg[i, j] < threshold:
                inputImg[i, j] = 0
            else:
                inputImg[i, j] = 255
    return inputImg