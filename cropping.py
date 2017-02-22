import argparse, cv2, imutils, numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# cropping
cropped = image[30:120, 240:335]
cv2.imshow("Cropped", cropped)

cv2.waitKey(0)
