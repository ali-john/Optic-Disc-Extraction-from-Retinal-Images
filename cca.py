import numpy as np
import cv2 as opencv
import random as r


def neighbours(i, j, src):
    # left
    left = src[i, j - 1]
    # top
    top = src[i - 1, j]
    # even diagonal
    diagE = src[i - 1, j - 1]
    # odd diagonal
    diagO = src[i - 1, j + 1]
    neighbour_array = [diagE, top, diagO, left]
    return neighbour_array


def Singlelabel(inputArr):
    output = 0
    for i in range(len(inputArr)):
        if inputArr[i] != 0:
            output = inputArr[i]
            break
    return output


def haveSameLabels(inputArr):
    temp = []
    for i in range(len(inputArr)):
        if inputArr[i] != 0:
            temp.append(inputArr[i])
    x = True
    for i in range(1, len(temp)):
        if temp[i] != temp[i - 1]:
            x = False
    return x


def MinMaxVal(inputArr):
    temp = []
    for i in range(len(inputArr)):
        if inputArr[i] != 0:
            temp.append(inputArr[i])
    output = [min(temp), max(temp)]
    return output


def colorObjects(labels):
    uniquelabels = np.unique(labels)
    colors = {1: (128, 0, 0), 2: (255, 255, 0), 3: (0, 255, 255), 4: (0, 255, 150), 5: (100, 128, 210)}
    colored_output = opencv.cvtColor(labels, opencv.COLOR_GRAY2BGR)
    for i in uniquelabels:
        if i == 0:
            continue
        else:
            x = r.randint(1, 5)
            for j in range(labels.shape[0]):
                for k in range(labels.shape[1]):
                    if labels[j, k] == i:
                        colored_output[j, k] = colors.get(x)

    return colored_output



def connectedComponentAnalysis(inputImg, Vset, start):
    vset = Vset
    # first pass
    label = np.zeros([inputImg.shape[0], inputImg.shape[1]], dtype="uint8")
    new_label = 0
    link = {}

    for i in range(start, inputImg.shape[0] - start):
        for j in range(start, inputImg.shape[1] - start):
            if inputImg[i, j] == vset:
                # no object
                current_neighbors = neighbours(i, j, label)
                if np.count_nonzero(current_neighbors) == 0:
                    new_label += 1
                    inputImg[i, j] = new_label
                    label[i, j] = new_label
                    link[new_label] = new_label
                # only one object - copy its label
                elif np.count_nonzero(current_neighbors) == 1:
                    label[i, j] = Singlelabel(current_neighbors)
                # more than one object
                elif np.count_nonzero(current_neighbors) > 1:
                    # objects have same labels
                    if haveSameLabels(current_neighbors):
                        label[i, j] = Singlelabel(current_neighbors)
                    # objects have different labels. Copy smallest label, replace largest label with smallest one
                    else:
                        label[i, j] = MinMaxVal(current_neighbors)[0]
                        link[(MinMaxVal(current_neighbors)[1])] = MinMaxVal(current_neighbors)[0]

    # Pass 2
    # Update link list.
    for key, value in link.items():
        if value == key:
            continue
        else:
            value = key
            temp = link.get(value)
            while value != temp:
                value = link.get(value)
                temp = link.get(value)
            link[key] = value

    # Update labels
    for i in range(start, label.shape[0] - start):
        for j in range(start, label.shape[1] - start):
            if label[i, j] != 0:
                label[i, j] = link.get(label[i, j])

    # Count objects
    obj = len(np.unique(label))
    return obj - 1, label
