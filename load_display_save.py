import argparse, cv2, os

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
ap.add_argument("-ni", "--new-image", required=False, help="Path to the image to be saved")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))

cv2.imshow("Image", image)
cv2.waitKey(0)

if args["new_image"]:
	try:
		cv2.imwrite(args["new_image"], image)
	except IOError as e:
		print("couldn't save new image {}: {}".format(args["new_image"], e.strerror))
	except:
		print("couldn't save new image")