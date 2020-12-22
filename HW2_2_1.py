from cv2 import cv2
from matplotlib import pyplot

# 水平翻轉
img1 = cv2.imread('test1.jpg')
flip_1 = cv2.flip(img1, 1)
cv2.imshow('test1_flip1.jpg', flip_1)
# 垂直翻轉
flip_2 = cv2.flip(img1, 0)
cv2.imshow('test1_flip2.jpg', flip_2)
# 水平+垂直翻轉
flip_3 = cv2.flip(img1, 1)
cv2.imshow('test1_flip3.jpg', flip_3)

# 90度旋轉
img2 = cv2.imread('test2.jpg')
rotate_1 = cv2.rotate(img2, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('test1_rotate90.jpg', rotate_1)
# 180度旋轉
rotate_2 = cv2.rotate(img2, cv2.ROTATE_180)
cv2.imshow('test1_rotate180.jpg', rotate_2)
# 270度旋轉
rotate_3 = cv2.rotate(img2, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow('test1_rotate270.jpg', rotate_3)

img3 =cv2.imread('test3.jpg')
crop_1=img3[0:240,0:426]
cv2.imshow('test1_crop_1.jpg',crop_1)

img3 =cv2.imread('test3.jpg')
crop_2=img3[240:480,426:852]
cv2.imshow('test1_crop_2.jpg',crop_2)

img3 =cv2.imread('test3.jpg')
crop_3=img3[480:720,852:1280]
cv2.imshow('test1_crop_3.jpg',crop_3)

cv2.imwrite('test1_flip1.jpg', flip_1)
cv2.imwrite('test1_flip2.jpg', flip_2)
cv2.imwrite('test1_flip3.jpg', flip_3)
cv2.imwrite('test1_rotate90.jpg', rotate_1)
cv2.imwrite('test1_rotate180.jpg', rotate_2)
cv2.imwrite('test1_rotate270.jpg', rotate_3)
cv2.imwrite('test1_crop_1.jpg',crop_1)
cv2.imwrite('test1_crop_2.jpg',crop_2)
cv2.imwrite('test1_crop_3.jpg',crop_3)

cv2.waitKey(0)
