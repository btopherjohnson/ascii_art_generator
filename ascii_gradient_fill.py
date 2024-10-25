import cv2 as cv
import numpy as np
import sys

#big width (400+), you want grad_mag_max / 16
#smaller width, you want grad_magmax / 2 - 8



if len(sys.argv) == 1: 
    print("You need to pass this program an argument, like this:")
    print("python3 ascii_gradient_canny.py igrad_mage.jpg")
    exit()
img = cv.imread(sys.argv[1])

ASCII_WIDTH = 200 #change this to change how many characters wide it is
height_over_width = np.shape(img)[0]/np.shape(img)[1]
ASCII_HEIGHT = int(ASCII_WIDTH * height_over_width) // 2 #characters in ascii are taller than they are wide

img = cv.resize(img, (ASCII_WIDTH, ASCII_HEIGHT))


bw = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


grad = np.gradient(bw) #first is up down, 2nd is left to right


grad_angle = np.angle(grad[1] + 1j * grad[0]) * 180 / np.pi
grad_mag = np.abs(grad[1] + 1j * grad[0])


outstr = ''
grad_mag_max = np.max(grad_mag)

def getchar(grad_angle):
    grad_angle += 90
    if grad_angle < 0:
        grad_angle += 180
    elif grad_angle > 180:
        grad_angle -= 180 

    if grad_angle < 30: 
        return '-'
    elif grad_angle < 75:
        return '\\'
    elif grad_angle < 135:
        return '|'
    elif grad_angle < 150:
        return '/'
    else: 
        return '-'

brush = ' .*#'

for i in range(len(grad_mag)):
    for j in range(len(grad_mag[0])):
        if grad_mag[i,j] < grad_mag_max / 8:
            outstr += brush[int(bw[i,j])*len(brush)//256]
        else:
            outstr += getchar(grad_angle[i,j])
    outstr += '\n'


cv.imwrite('trash.jpg', grad_mag)

cv.waitKey(-1)

#print(outstr)

file = open('trash_fill.txt', 'w')
file.write(outstr)
file.close()

print("you can find your ascii art in trash_fill.txt")
