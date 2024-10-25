import cv2 as cv
import numpy as np
import sys

if len(sys.argv) == 1: 
    print("You need to pass this program an argument, like this:")
    print("python3 ascii_gradient_canny.py image.jpg")
    exit()
img = cv.imread(sys.argv[1])

ASCII_WIDTH = 200 #change this to change how many characters wide it is
height_over_width = np.shape(img)[0]/np.shape(img)[1]
ASCII_HEIGHT = int(ASCII_WIDTH * height_over_width) // 2 #because characters are around 2x as high as wide

bw = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

bw = cv.GaussianBlur(bw, (5, 5), -1)

bw_small = cv.resize(bw, (ASCII_WIDTH, ASCII_HEIGHT))
bw_small_can = cv.Canny(bw_small, 50, 200)


grad = np.gradient(bw_small_can) #first is up down, 2nd is left to right
print(np.shape(grad))
angle = np.angle(grad[1] + 1j * grad[0]) * 180 / np.pi
angle = angle + 179
print(np.shape(angle))
print(np.max(angle), np.min(angle))

brushes = "|/-\\|/-\\|"
outstr = ''

for i in range(len(bw_small)):
    for j in range(len(bw_small[0])):
        if bw_small_can[i,j] == 0:
            outstr += ' '
        else:
            outstr += brushes[int(angle[i,j]*len(brushes))//360]
    outstr += '\n'


cv.imshow('lol', bw_small_can)
cv.imshow('lol2', bw_small)


cv.waitKey(-1)

file = open('trash_can.txt', 'w')
file.write(outstr)
file.close()

print("you can find your ascii art in trash_can.txt")

