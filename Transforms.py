import numpy as np


def logT(image):
    max_value = np.amax(image)
    output = np.zeros([image.shape[0], image.shape[1]], dtype=np.uint8)
    c = 255 / np.log(1 + max_value)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            s = c * np.log(image[i, j] + 1)
            output[i, j] = s
    return output


def powerLaw(image, gamma):
    output = np.array(255 * (image / 255) ** gamma, dtype=np.uint8)
    return output


def minFilter(img, size):
    out = np.zeros([img.shape[0], img.shape[1]], dtype="uint8")
    for i in range(img.shape[0] - size):
        for j in range(img.shape[1] - size):
            mat = img[i: i + size, j: j + size]
            mat = np.ravel(mat)  # convert to 1D array
            mat = np.sort(mat)
            out[i, j] = np.min(mat)
    return out


def maxFilter(img, size):
    out = np.zeros([img.shape[0], img.shape[1]], dtype="int")
    for i in range(img.shape[0] - size):
        for j in range(img.shape[1] - size):
            mat = img[i: i + size, j: j + size]
            mat = np.ravel(mat)  # convert to 1D array
            mat = np.sort(mat)
            out[i, j] = np.max(mat)
    return out


def ContrastStretching(image, lp, hp):
    lower_percentile = np.percentile(image, lp)  # used as min value
    higher_percentile = np.percentile(image, hp)  # used for max value
    output = np.zeros([image.shape[0], image.shape[1]], dtype=np.uint8)
    # pixel value less than lp percentile -- set to 0
    # pixel value > hp percentile -- set to 255
    # 5th percentile < pixel value < 95th percentile -- stretch according to formula
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            val = image[i, j]
            if val < lower_percentile:
                output[i, j] = 0
            elif val > higher_percentile:
                output[i, j] = 255
            else:
                output[i, j] = ((image[i, j] - lower_percentile) / (higher_percentile - lower_percentile)) * 255
    return output
