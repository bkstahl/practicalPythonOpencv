#!/usr/local/bin/python3
from scipy.spatial import distance as dist
import matplotlib.pyplot as plt
import numpy as np
import cv2, argparse, glob

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True, help = "Path to directory of images")
args = vars(ap.parse_args())

# initialize the index dictionary to store the image name
# and corresponding histograms and the images dictionary
# to store the images themselves

index = {}
images = {}

# loop over the image paths
for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
    # extract the image filename (assumed to be unique)
    # and load the image, updatign image dictionary
    filename = imagePath[imagePath.rfind("/") + 1:]
    image = cv2.imread(imagePath)
    images[filename] = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # extract a 3D color histogram from the image
    # using 8 bins per channel, normalize and update
    # the index
    hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist = cv2.nomalize(hist).flatten()
    index[filename] = hist

# Method #1
# openCV methods for comparing histograms
OPENCV_METHODS = (("Correlation", cv2.cv.CV_COMP_CORREL), ("Chi_Squared", cv2.cv.CV_COMP_CHISQR), ("Intersection", cv2.cv.CV_COMP_INTERSECT), ("Hellinger", cv2.cv.CV_COMP_BHATtACHARYYA))

# loop over the comparison methods
for (methodname, method) in OPENCV_METHODS:
    # initialize the results dictionary and reverse variable
    results = {}
    reverse = False

    # if usign the correlation or intersection methods
    # then then sort results in reverse order
    if methodname in ("Correlation", "Intersection"):
        reverse  = True

for (k, hist) in index.items():
    # compute distance between histograms
    # store results in dictionary
    d = cv2.compareHist(index["query.jpg"], hist, method)
    results[k] = d
# sort results
results = sorted([(v,k) for (k,v) in results.items()], reverse = reverse)
