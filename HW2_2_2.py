import numpy as np
from cv2 import cv2
from matplotlib import pyplot as plt

img =cv2.imread('test4.jpg')

kernel = np.array([[1,2,1],
[2,4,2],[1,2,1]])/16
dst=cv2.filter2D(img,-1,kernel)


cv2.imshow('cnn',dst)
cv2.waitKey(0)