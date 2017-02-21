import argparse, cv2, numpy as np, imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# scaling
# scaling without helper function
ratio = 150.0 / image.shape[1]
dim = (150, int(image.shape[0] * ratio))

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized (width)", resized)

# scaled with helper function
resized = imutils.scale(image, width = 400)
cv2.imshow("Resized (height)", resized)

cv2.waitKey(0)
