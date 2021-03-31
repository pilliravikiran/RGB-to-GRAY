import cv2
import glob
images_path=glob.glob("/path/*") #path to load bulk of images to convert from BGR to GRAY.
i=0
for image in images_path:
	img=cv2.imread(image)
	gray_images=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	cv2.imwrite('/path/%i.jpg'%i,gray_images)     # Path to store converted GRAY images.
	i=i+1
	
	cv2.destroyAllWindows()