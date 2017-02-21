import numpy as np
import cv2

def translate(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted

def rotate(image, angle, center = None, scale = 1):
    if center is None:
        (w, h) = (image.shape[1], image.shape[0])
        center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated

def scale(image, width = None, height = None, intrp = cv2.INTER_AREA):
    if width is None and height is None:
        return image
    if width is not None and height is not None:
        dim  = (width, height)
    elif width is not None:
        r = float(width) / image.shape[1]
        dim = (width, int(image.shape[0] * r))
    else:
        r = float(height) / image.shape[0]
        dim = (int(image.shape[1] * r), height)
    scaled = cv2.resize(image, dim, interpolation = intrp)
    return scaled
