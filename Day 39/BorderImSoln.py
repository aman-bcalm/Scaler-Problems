import numpy as np
import pandas as pd
import cv2


img = cv2.imread('resized_nearest.jpg')
borderoutput = cv2.copyMakeBorder(
    img, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=[0, 0, 0])

cv2.imwrite('output.png', borderoutput)

bd_diff = borderoutput.reshape((borderoutput.shape[0]*borderoutput.shape[1]), borderoutput.shape[2])

df = pd.DataFrame(bd_diff, columns = ['c1', 'c2', 'c3'])

df.to_csv('result.csv', index = False)