#!/usr/local/bin/python3
import argparse, cv2, numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# masking
# creating mask by drawing a rectangle
mask = np.zeros(image.shape[:2], dtype = "uint8")
(cx, cy) = (image.shape[1]//2, image.shape[0]//2)
cv2.rectangle(mask, (cx-75, cy-75), (cx+75, cy+75), 255, -1)
cv2.imshow("Mask rectangle", mask)

# applying mask to image
masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Masked by rectangle", masked)

#creating mask by drawing a circle
mask = np.zeros(image.shape[:2], dtype = "uint8")
(cx, cy) = (image.shape[1]//2, image.shape[0]//2)
cv2.circle(mask, (cx, cy), 75, 255, -1)
cv2.imshow("Mask circle", mask)

# applying mask to image
masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Masked by circle", masked)

cv2.waitKey(0)
