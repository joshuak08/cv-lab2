import cv2
import numpy as np

image = cv2.imread('car1.png')

blur = cv2.GaussianBlur(image,(5,5),0)

new = image*4 - 3*blur

cv2.imshow("sharpened", new)
cv2.waitKey()
cv2.destroyAllWindows()