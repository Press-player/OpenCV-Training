import cv2
import numpy as np

dispW =360
dispH =240
flip =2

img1 =np.zeros((240,360,3),np.uint8)
img1[0:240,0:360]=[255,233,0]
#img1[100:140,160:200]=[255]


#img2 =np.zeros((240,360,1),np.uint8)
#img2[0:240,0:360]=[255]
#mg2[0:240,0:180]=[255]
#bitAnd =cv2.bitwise_and(img2,img1)
#bitOr =cv2.bitwise_or(img2,img1)
#bitXor =cv2.bitwise_xor(img1,img2)

def click(event,x,y,flags,params):
    global rgb
    global evt
   
    if event==cv2.EVENT_LBUTTONDOWN:
        blue =int(frame[y,x,0])
        green =int(frame[y,x,1])
        red =int(frame[y,x,2])
        rgb =(red,green,blue)
        print('Color: ',rgb)
        img1[0:240,0:360]=rgb


camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam =cv2.VideoCapture(camSet)
cv2.namedWindow('piCam')
cv2.setMouseCallback('piCam',click)

while True:
    ret,frame =cam.read()

    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0)
    cv2.imshow('img1',img1)
    cv2.moveWindow('img1',0,300)

    frame2 =cv2.bitwise_or(frame,img1)
    cv2.imshow('piCam2',frame2)
    cv2.moveWindow('piCam2',480,0)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
