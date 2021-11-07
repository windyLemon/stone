import cv2
import numpy as np
from skimage.feature import peak_local_max
from skimage.morphology import watershed
from scipy import ndimage
import numpy as np
import imutils
from PIL import Image
import matplotlib.pyplot as plt
from preprocess import preprocess
import random


scale = (1 / 6.3)
def auto_canny(image, sigma=0.5):
    # compute the median of the single channel pixel intensities
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.bilateralFilter(src=image, d=-1, sigmaColor=30, sigmaSpace=0.05)
    image = cv2.GaussianBlur(image, (3, 3), 0)

    # apply automatic Canny edge detection using the computed median
    # lower = int(max(0, (1.0 - sigma) * v))
    # upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, 20, 100)
    # edged = cv2.medianBlur(edged, 3)
    return edged
    # return image


def binary_image(image, t1=75, t2=15):
    # image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 725, 15)
    # image = 255 - image
    image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, t1, t2)
    # image = cv2.medianBlur(image, 3)
    contours, hierarch = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    for i in range(len(contours)):
        area = cv2.contourArea(contours[i])  # 计算轮廓所占面积
        if area < 300:  # 将area小于阈值区域填充背景色，由于OpenCV读出的是BGR值
            cv2.drawContours(image, [contours[i]], -1, 0, thickness=-1)  # 原始图片背景BGR值(84,1,68)
            continue
    image = 255 - image
    contours, hierarch = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    for i in range(len(contours)):
        area = cv2.contourArea(contours[i])  # 计算轮廓所占面积
        if area < 300:  # 将area小于阈值区域填充背景色，由于OpenCV读出的是BGR值
            cv2.drawContours(image, [contours[i]], -1, 0, thickness=-1)  # 原始图片背景BGR值(84,1,68)
            continue
    return image


def segmentation(image, original):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel, iterations=2)
    sure_bg = cv2.dilate(opening, kernel, iterations=2)

    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    cv2.normalize(dist_transform, dist_transform, 0, 1.0, cv2.NORM_MINMAX)
    dist_transform = cv2.bilateralFilter(src=dist_transform, d=-1, sigmaColor=30, sigmaSpace=0.05)
    ret, sure_fg = cv2.threshold(dist_transform, 0.4 * dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)
    ret, v = cv2.connectedComponents(sure_fg, connectivity=8)
    v += 1
    v[unknown==255] = 0
    final = cv2.watershed(original, v)
    original[final == -1] = [255, 255, 0]
    # calculate(v, original, final)
    total = np.max(v) - np.min(v) - 2
    for i in range(2, total + 2):
        original[v == i] = random.randint(0, 255)
    return v, original, final


def calculate(v, final):
    total = np.max(v) - np.min(v) - 2
    res = []
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    for i in range(2, total + 2):
        area = np.sum(v == i)
        mask = np.uint8((v == i) * 255)
        if mask.sum() == 0:
            continue
        mask = cv2.dilate(mask, kernel)
        l = np.sum((mask == 255) & (final == -1))
        d = (4 * area / l) * scale
        res.append(d)
    return res


def algorithm_watershed(image):
    c = auto_canny(image)
    original = image
    image = preprocess(image, adapt_median=False)
    image = binary_image(image, 725, 15)
    # image[c == 255] = 0
    v, image, final = segmentation(image, original=original)

    # v[v == 1] = 0
    # v[v != 0] = 255
    # v = np.uint8(v)
    # counters, hierarchy = cv2.findContours(v, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    return v, final


if __name__ == '__main__':
    imagePath = '/Users/jhchen/PycharmProjects/stones/Desktop/temp/img5.bmp'
    # imagePath = '/Users/jhchen/PycharmProjects/stones/Desktop/seg2/01背景.bmp'
    # imagePath = 'qin.jpg'
    image = cv2.imread(imagePath)
    # # c = auto_canny(image)
    # original = image
    image = preprocess(image, adapt_median=False)
    image = binary_image(image, 725, 15) #- binary_image(image, 225, 15)
    # # image[c==255] = 0
    # _, image, _ = segmentation(image, original=original)

    # v, final = algorithm_watershed(image)
    # calculate(v, final)

    cv2.namedWindow('Edges', cv2.WINDOW_NORMAL)
    cv2.imshow("Edges", image)
    cv2.waitKey(0)