import cv2
import numpy as np

#------------------------------------Setup Variables-------------------------------------
dispW =360
dispH =240
flip =2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam =cv2.VideoCapture(camSet)
#--------------------------------------------------------------------------------------------

while True:
    ret,frame =cam.read()
#------------------------Show Frames from PiCam------------------------------------------------------------
    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
