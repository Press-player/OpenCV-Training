import cv2
import numpy as np

dispW =360
dispH =240
flip =2

img1 =np.zeros((240,360,1),np.uint8)
#img1[0:240,0:360]=[255]
img1[100:140,160:200]=[255]


img2 =np.zeros((240,360,1),np.uint8)
#img2[0:240,0:360]=[255]
img2[0:240,0:180]=[255]
bitAnd =cv2.bitwise_and(img2,img1)
bitOr =cv2.bitwise_or(img2,img1)
bitXor =cv2.bitwise_xor(img1,img2)

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam =cv2.VideoCapture(camSet)

while True:
    ret,frame =cam.read()
    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0)
    cv2.imshow('img1',img1)
    cv2.moveWindow('img1',0,300)
    cv2.imshow('img2',img2)
    cv2.moveWindow('img2',420,0)
    cv2.imshow('and',bitAnd)
    cv2.moveWindow('and',420,300)
    cv2.imshow('or',bitOr)
    cv2.moveWindow('or',780,0)
    cv2.imshow('xor',bitXor)
    cv2.moveWindow('xor',780,300)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
