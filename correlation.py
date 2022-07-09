import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('C:\Users\Admin\Desktop\Obj+TL+Cam_4_blue.bmp')
blur = cv.blur(img,(5,5))
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()