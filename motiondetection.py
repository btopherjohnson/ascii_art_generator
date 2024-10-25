import cv2 as cv
import numpy as np


cam = cv.VideoCapture(0) 
result,last = cam.read()
if(result):
    last = cv.cvtColor(last, cv.COLOR_BGR2GRAY)
    last = cv.GaussianBlur(last, (5,5), 0)


while(result):

    result,img = cam.read() 
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    current = cv.GaussianBlur(gray, (5,5), 0)

    diff = cv.absdiff(current, last)
    filt = np.ones((5,5))
    diff = cv.dilate(diff, filt)
    diff = cv.threshold(diff, 20, 255, cv.THRESH_BINARY)[1]
    contours, _ = cv.findContours(diff, cv.RETR_EXTERNAL, method=cv.CHAIN_APPROX_SIMPLE)
    
    cv.drawContours(img, contours, -1, (0, 255, 0), 2, cv.LINE_AA)

    cv.imshow('img', img)

    if cv.waitKey(30) != -1:
        break


    last = current



cam.release()
