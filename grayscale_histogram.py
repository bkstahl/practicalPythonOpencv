#!/usr/local/bin/python3
import argparse, cv2
import numpy as np
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help="Path to image file")
args = vars(ap.parse_args())

image = cv2.cvtColor(cv2.imread(args["image"]), cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", image)

hist = cv2.calcHist([image], [0], None, [256], [0, 256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)
