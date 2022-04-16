import cv2
import numpy as np

#------------------------------------Setup Variables-------------------------------------
dispW =360
dispH =240
flip =2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam =cv2.VideoCapture(camSet)
def nothing(x):
    pass
cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars',500,0)
cv2.createTrackbar('hueLower1','Trackbars',0,179,nothing)
cv2.createTrackbar('hueHigher1','Trackbars',0,179,nothing)
cv2.createTrackbar('hueLower2','Trackbars',0,179,nothing)
cv2.createTrackbar('hueHigher2','Trackbars',0,179,nothing)
cv2.createTrackbar('satLower','Trackbars',0,255,nothing)
cv2.createTrackbar('satHigher','Trackbars',0,255,nothing)
cv2.createTrackbar('valLow','Trackbars',0,255,nothing)
cv2.createTrackbar('valHigh','Trackbars',0,255,nothing)

while True:
    ret,frame =cam.read()


#------------------------Show Frames from PiCam------------------------------------------------------------

    
    hsv =cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #print(hsv)
    hueLow1 =cv2.getTrackbarPos('hueLower1','Trackbars')
    hueHigh1 =cv2.getTrackbarPos('hueHigher1','Trackbars')

    hueLow2 =cv2.getTrackbarPos('hueLower2','Trackbars')
    hueHigh2 =cv2.getTrackbarPos('hueHigher2','Trackbars')

    Ls =cv2.getTrackbarPos('satLower','Trackbars')
    Hs =cv2.getTrackbarPos('satHigher','Trackbars')
 
    Lv =cv2.getTrackbarPos('valLow','Trackbars')
    Hv =cv2.getTrackbarPos('valHigh','Trackbars')
 
    l_b1 =np.array([hueLow1,Ls,Lv],np.uint8)
    h_b1 =np.array([hueHigh1,Hs,Hv],np.uint8)

    l_b2 =np.array([hueLow2,Ls,Lv],np.uint8)
    h_b2 =np.array([hueHigh2,Hs,Hv],np.uint8)

    FGmask1 =cv2.inRange(hsv,l_b1,h_b1)
    FGmask2 =cv2.inRange(hsv,l_b2,h_b2)

    FGmaskComplete =cv2.add(FGmask1,FGmask2)
    postMask =cv2.bitwise_and(frame,frame,mask=FGmaskComplete)

    BGmaskComplete =cv2.bitwise_not(FGmaskComplete)
    BGComplete =cv2.cvtColor(BGmaskComplete,cv2.COLOR_GRAY2BGR)
    
    contours, hierarchy =cv2.findContours(FGmaskComplete,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours =sorted(contours,key=lambda x:cv2.contourArea(x),reverse =True)
    
    for cnt in contours:
        area =cv2.contourArea(cnt)
        (x,y,w,h) = cv2.boundingRect(cnt)
        if area>=80:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
            #cv2.drawContours(frame,[cnt],0,(0,255,0),3)

    #cv2.drawContours(frame,contours,0,(255,0,0),3)

    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0)
    finalWindow =cv2.add(postMask,BGComplete)
    cv2.imshow('FinalWindow',finalWindow)
    cv2.moveWindow('FinalWindow',900,0)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
