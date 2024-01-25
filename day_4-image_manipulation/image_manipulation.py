#import the necessary libraries
import cv2
import numpy as np


# store the image you want to edit in a variable
image = cv2.imread('day_4-image_manipulation\cat.jpg')


# decide the height and width you want ot resize your image to
width = 2200
height = 1200

#resize the image with cv2 resize function passing in the image and the width and height needed
resized_img = cv2.resize(image, (width, height))


# to rotate the image
rotate = 0
row, col = image.shape[:2]


# using the size you want to rotate the img to and also the row and column of the image
# get the dimension you want it to fit 
rotated_matrix = cv2.getRotationMatrix2D((col / 2, row / 2), rotate, 1)
rotate_img = cv2.warpAffine(resized_img, rotated_matrix, (col, row))


# sample of how we add effect to our image
blurred = cv2.GaussianBlur(resized_img, (5,5), 0)


# here we save our new image as output 
cv2.imwrite("output.jpg", rotate_img)
