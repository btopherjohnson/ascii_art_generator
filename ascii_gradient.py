import cv2 as cv
import numpy as np
import sys

#big width (400+), you want mag_max / 16
#smaller width, you want magmax / 2 - 8



if len(sys.argv) == 1: 
    print("You need to pass this program an argument, like this:")
    print("python3 ascii_gradient_canny.py image.jpg")
    exit()
img = cv.imread(sys.argv[1])

ASCII_WIDTH = 200 #change this to change how many characters wide it is
height_over_width = np.shape(img)[0]/np.shape(img)[1]
ASCII_HEIGHT = int(ASCII_WIDTH * height_over_width) // 2 #characters in ascii are taller than they are wide

img = cv.resize(img, (ASCII_WIDTH, ASCII_HEIGHT))


bw = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


grad = np.gradient(bw) #first is up down, 2nd is left to right


angle = np.angle(grad[1] + 1j * grad[0]) * 180 / np.pi
mag = np.abs(grad[1] + 1j * grad[0])


outstr = ''
mag_max = np.max(mag)

def getchar(angle):
    angle += 90
    if angle < 0:
        angle += 180
    elif angle > 180:
        angle -= 180 

    if angle < 30: 
        return '-'
    elif angle < 75:
        return '\\'
    elif angle < 135:
        return '|'
    elif angle < 150:
        return '/'
    else: 
        return '-'

for i in range(len(mag)):
    for j in range(len(mag[0])):
        if mag[i,j] < mag_max / 8:
            outstr += ' '
        else:
            outstr += getchar(angle[i,j])
    outstr += '\n'


cv.imwrite('trash.jpg', mag)

cv.waitKey(-1)

#print(outstr)

file = open('trash_grad.txt', 'w')
file.write(outstr)
file.close()

print("you can find your ascii art in trash_grad.txt")
