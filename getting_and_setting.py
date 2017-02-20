import argparse, cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

#getting and setting pixel color
(b, g, r) = image[219,90]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

image [0, 0] = (0, 0, 255)
(b, g, r) = image[0,0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

cv2.imshow("Image", image)
cv2.waitKey(0)

#cropping a slice of the image
corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)
cv2.waitKey(0)

#setting the pixel color of a slice
image[0:200, 0:50] = (0, 255, 0)
cv2.imshow("Updated", image)
cv2.waitKey(0)