import cv2
import numpy as np

#------------------------------------Setup Variables-------------------------------------
dispW =360
dispH =240
flip =2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam =cv2.VideoCapture(camSet)
blank = np.zeros([240,360,1],np.uint8)
#blank[100:140,140:180] =[100]

while True:
    ret,frame =cam.read()
    
   # print(frame.shape)
    b,g,r =cv2.split(frame)
    g[:]=g[:]*.6
    blue =cv2.merge((b,blank,blank))
    red =cv2.merge((blank,blank,r))
    green =cv2.merge((blank,g,blank))
    merge =cv2.merge((b,g,r))
#------------------------Show Frames from PiCam------------------------------------------------------------
    cv2.imshow('merge',merge)
    cv2.moveWindow('merge',800,0)
    cv2.imshow('blue',blue)
    cv2.moveWindow('blue',440,0)
    cv2.imshow('green',green)
    cv2.moveWindow('green',0,300)
    cv2.imshow('red',red)
    cv2.moveWindow('red',440,300)


    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
