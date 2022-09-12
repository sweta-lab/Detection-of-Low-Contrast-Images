from skimage.exposure import is_low_contrast
import cv2
import matplotlib.pyplot as plt

#read input images and convert to grayscale
image1 = cv2.imread('low_contrast_image.jpg')
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
image2 = cv2.imread('high_contrast_image.jpg')
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

#plot histograms of the input images
plt.hist(gray1.ravel(),256,[0,256]); plt.show()
plt.hist(gray2.ravel(),256,[0,256]); plt.show()

#provide the low contrast fraction threshold
#An image is considered low- contrast when its range of 
#brightness spans less than this fraction of its data type’s full range.
fraction_threshold = 0.5

#Use the is_low_contrast function to determine level of contrast
#I set the fraction threshold manually
if is_low_contrast(gray1, 0.50):
    print('Low contrast image')
else:
    print('High contrast image')

if is_low_contrast(gray2, 0.50):
    print('Low contrast image')
else:
    print('High contrast image')




