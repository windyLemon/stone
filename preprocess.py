import cv2
import numpy as np


def AdaptProcess(src, i, j, minSize, maxSize):

    filter_size = minSize

    kernelSize = filter_size // 2
    rio = src[i-kernelSize:i+kernelSize+1, j-kernelSize:j+kernelSize+1]
    minPix = np.min(rio)
    maxPix = np.max(rio)
    medPix = np.median(rio)
    zxy = src[i, j]

    if (medPix > minPix) and (medPix < maxPix):
        if (zxy > minPix) and (zxy < maxPix):
            return zxy
        else:
            return medPix
    else:
        filter_size = filter_size + 2
        if filter_size <= maxSize:
            return AdaptProcess(src, i, j, filter_size, maxSize)
        else:
            return medPix


def adapt_median_filter(img, minsize, maxsize):

    borderSize = maxsize // 2

    src = cv2.copyMakeBorder(img, borderSize, borderSize, borderSize, borderSize, cv2.BORDER_REFLECT)

    for m in range(borderSize, src.shape[0] - borderSize):
        for n in range(borderSize, src.shape[1] - borderSize):
            src[m,n] = AdaptProcess(src, m, n, minsize, maxsize)

    dst = src[borderSize:borderSize+img.shape[0], borderSize:borderSize+img.shape[1]]
    return dst


def preprocess(image, adapt_median=False):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.bilateralFilter(src=image, d=-1, sigmaColor=30, sigmaSpace=0.05)
    if adapt_median:
        image = adapt_median_filter(image, minsize=3, maxsize=7)
    else:
        image = cv2.medianBlur(image, 3)
    return image
