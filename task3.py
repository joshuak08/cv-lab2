import numpy as np
import cv2
import statistics

image = cv2.imread("car2.png", cv2.IMREAD_GRAYSCALE)

y = image.shape[0]
x = image.shape[1]

image = np.pad(image, 1, mode='constant')

output = np.zeros([y, x], dtype=np.float32)

def medianFilter(x, y):
    output = []
    gauss = 1/9

    for i in range(-1, 2): # y
        for j in range(-1, 2): #x
            output.append(image[y+i][x+j])
    return statistics.median(output)


for i in range(1, y+1): #y
    for j in range(1, x+1): #x
        output[j-1][i-1] = medianFilter(i, j)

# sussy monki OOOO yeahhh bosss

cv2.imshow('median', output)
cv2.waitKey()
cv2.destroyAllWindows()