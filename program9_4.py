import numpy as np
import cv2

cols = 640
rows = 480
image = np.zeros((rows, cols, 3), np.uint8)

image[:,:] = [128, 0, 0]

image[0:240,0:320] = [0, 128, 0]

image[240:480:2, 320:640:2] = [0, 128, 128]

cv2.imshow("image", image)
