import cv2 as cv
import numpy as np
import sys

img = cv.imread(sys.argv[1])

ASCII_WIDTH = 90*2
height_over_width = np.shape(img)[0]/np.shape(img)[1]
ASCII_HEIGHT = int(ASCII_WIDTH * height_over_width) // 2

bw = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
bw_small = cv.resize(bw, (ASCII_HEIGHT, ASCII_WIDTH))


brushes = " `^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
outstr = ''
for i in bw_small:
    for j in i:
        outstr += brushes[(int(j)*len(brushes))//256]
    outstr += '\n'


#cv.imshow('lol', bw_small)


#cv.waitKey(-1)

#print(outstr)

file = open('trash.txt', 'w')
file.write(outstr)
file.close()