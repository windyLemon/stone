import numpy as np
from PIL import Image
import random
from skimage import transform as sktsf


def read_image(path, dtype=np.float32, color=True):


    f = Image.open(path)
    try:
        if color:
            img = f.convert('RGB')
        else:
            img = f.convert('P')
        img = np.asarray(img, dtype=dtype)
    finally:
        if hasattr(f, 'close'):
            f.close()

    if img.ndim == 2:
        # reshape (H, W) -> (1, H, W)
        return img[np.newaxis]
    else:
        # transpose (H, W, C) -> (C, H, W)
        return img.transpose((2, 0, 1))




def random_flip(img, y_random=False, x_random=False
                 ):

    y_flip, x_flip = False, False
    if y_random:
        y_flip = random.choice([True, False])
    if x_random:
        x_flip = random.choice([True, False])

    if y_flip:
        img = img[:, ::-1, :]
    if x_flip:
        img = img[:, :, ::-1]

    return img


def random_rotate(img,rotate_random=False):
    rotate = False
    if rotate_random:
        rotate = random.choice([True, False])


    if rotate:
        angel = random.choice([0, 180])
        img = sktsf.rotate(img,angel)


    return img