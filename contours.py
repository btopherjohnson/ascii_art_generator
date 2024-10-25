import cv2
import sys
import numpy as np
import cv2

if (len(sys.argv) == 1):
    print('try again')
    exit()

img = cv2.imread(sys.argv[1])

img = cv2.resize(img, (np.shape(img)[1]//4, np.shape(img)[0]//4))

blurry = cv2.blur(img,(5,5)) #cv2.GaussianBlur(img, (5, 5), 255)
blurry = cv2.blur(blurry,(5,5)) #cv2.GaussianBlur(img, (5, 5), 255)

bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

lines = cv2.Canny(blurry, 20, 100)
ret, new = cv2.threshold(lines, 100, 255, cv2.THRESH_BINARY_INV)
#ret, thresh = cv2.threshold(bw, 150, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(new, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
new = np.zeros_like(img)

#cv2.drawContours(new, contours, -1, (0,255,0), 2, -1)




'''
for c in contours:
    mask = np.zeros(bw.shape,np.uint8)
    cv2.drawContours(mask,[c],0,255,-1)
    color = cv2.mean(img, mask=mask)
    cv2.drawContours(new, [c], 0, color, -1)
    '''


cv2.imshow('lol', img)

oil = cv2.xphoto.oilPainting(img, 10, 10)
cv2.imshow('oil', oil)
cv2.waitKey(-1)