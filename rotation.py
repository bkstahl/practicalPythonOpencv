import argparse, cv2, numpy as np, imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# rotation
# rotation via matrices
(h, w) = image.shape[:2]
center  = (w//2, h//2)

# rotated with matrices
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated 45 degrees", rotated)

M = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated -90 degrees", rotated)

# rotated with helper function
rotated = imutils.rotate(image, -180)
cv2.imshow("Rotated -180 degrees", rotated)

cv2.waitKey(0)
