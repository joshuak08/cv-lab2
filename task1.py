import numpy as np
import cv2

image = cv2.imread("mandrill.jpg", cv2.IMREAD_GRAYSCALE)

y = image.shape[0]
x = image.shape[1]

image = np.pad(image, 1, mode='constant')

output = np.zeros([y, x], dtype=np.float32)

def convolve(x, y):
    output = 0
    gauss = 1/9

    for i in range(-1, 2): # y
        for j in range(-1, 2): #x
            output += image[y+i][x+j]
    return output/9


for i in range(1, y+1): #y
    for j in range(1, x+1): #x

        output[j-1][i-1] = convolve(i, j)


print(np.rint(output))

cv2.imwrite('gaussian_blur.jpg', np.rint(output))