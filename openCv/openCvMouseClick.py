import cv2
import numpy as np
evt =-1
coord =[]
img =np.zeros((250,250,3),np.uint8)

def click(event,x,y,flags,params):
    global pnt
    global evt
   
    if event==cv2.EVENT_LBUTTONDOWN:
        #print("Mouse event was: ",event)
        #print("x: ",x," y: ",y)
        pnt =(x,y)
        coord.append(pnt)
        evt =event
    if  event==cv2.EVENT_RBUTTONDOWN:
        blue =int(frame[y,x,0])
        green =int(frame[y,x,1])
        red =int(frame[y,x,2])
        colorValues =str(blue)+', '+str(green)+', '+str(red)
        img[:]=[blue,green,red]
        font2 =cv2.FONT_HERSHEY_PLAIN
        r =255-red
        g =255-green
        b =255-blue
        rgb =(r,g,b)
        cv2.putText(img,colorValues,(10,25),font2,1,rgb,2)
        cv2.imshow('newFrame',img)

dispW =960
dispH =700
flip =2


cv2.namedWindow('piCam')
cv2.setMouseCallback('piCam',click)
font =cv2.FONT_HERSHEY_PLAIN

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam =cv2.VideoCapture(camSet)
while True:
    ret,frame =cam.read()

    if evt==1:
        for i in coord:
                cv2.circle(frame,i,5,(255,255,255),-1)
                position =str(i)
                cv2.putText(frame,position,i,font,3,(255,0,100),2)

    cv2.moveWindow('piCam',0,0)
    cv2.imshow('piCam',frame)
    keyEvent =cv2.waitKey(1)
    if keyEvent==ord('q'):
        break
    if keyEvent==ord('c'):
        coord=[]
cam.release()
cv2.destroyAllWindows()