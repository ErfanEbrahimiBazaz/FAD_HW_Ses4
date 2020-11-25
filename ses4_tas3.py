import numpy as np
import cv2 as cv


img_path = r'C:\Users\E17538\OneDrive - Uniper SE\Desktop\DailyActivities\FAD\Sol_ses3\base.png'
img = cv.imread(img_path, 1)
cv.imshow('base image', img)

# apply bilateral filter to smooth texture
d = 11
bilateral_img = cv.bilateralFilter(img, d, 75, 75)
cv.imshow('bilateral filter on original img', bilateral_img)
cv.imwrite('bilat.jpg', bilateral_img)


# apply median rank to bilateral output to denoise more but keep the border
ksize = 3
median_bilat_img = cv.medianBlur(bilateral_img, ksize=ksize)
cv.imshow('Median blur on bilat', median_bilat_img)
cv.imwrite('med.jpg', median_bilat_img)


cv.waitKey(delay=0) == '27'
cv.destroyAllWindows()