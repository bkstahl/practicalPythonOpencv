import argparse, cv2, os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
ap.add_argument("-ni", "--new-image", required=False, help="Path to the image to be saved")
args = vars(ap.parse_args())
	
image = cv2.imread(args["image"])
# converted the order on the colors from opencv to matplotlib prior to showing
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) 
plt.show()