import cv2
import numpy as np

#------------------------------------Setup Variables-------------------------------------
dispW =360
dispH =240
flip =2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam =cv2.VideoCapture(camSet)
cv2.namedWindow('Blended')
#---------------------------------------------------------------------------------------------
def nothing(x):
  pass

cv2.createTrackbar('BlendedValue', 'Blended',0,100,nothing)
cvLogo =cv2.imread('cv.jpg')
cvLogo =cv2.resize(cvLogo,(360,240))
cvLogoGray =cv2.cvtColor(cvLogo,cv2.COLOR_BGR2GRAY)
#cv2.imshow('cv Logo Gray',cvLogoGray)
#cv2.moveWindow('cv Logo Gray',0,300)

_,BGMask =cv2.threshold(cvLogoGray,220,255,cv2.THRESH_BINARY)
cv2.imshow('BG Mask',BGMask)
cv2.moveWindow('BG Mask',0,300)

FGMask =cv2.bitwise_not(BGMask)
#cv2.imshow('FG Mask',FGMask)
#cv2.moveWindow('FG Mask',790,0)

FG =cv2.bitwise_and(cvLogo,cvLogo,mask =FGMask)
cv2.imshow('FG Original',FG)
cv2.moveWindow('FG Original',420,300)


while True:
    ret,frame =cam.read()

    BG =cv2.bitwise_and(frame,frame,mask =BGMask)
    FG1 =cv2.bitwise_and(frame,frame,mask =FGMask)    
#------------------------Show Frames from PiCam------------------------------------------------------------
    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0)

    #BGMaskCam =cv2.bitwise_and(frame,BGMask)
    cv2.imshow('BG MaskCam',BG)
    cv2.moveWindow('BG MaskCam',420,0)

  #  cv2.imshow('FG MaskCam',FG1)
  # cv2.moveWindow('FG MaskCam',790,580)


    compImage =cv2.add(BG,FG)
    #cv2.imshow('BG/FG',compImage)
    #cv2.moveWindow('BG/FG',780,300)



    BV =cv2.getTrackbarPos('BlendedValue','Blended')/100
    BV2 =1-BV
    Blended =cv2.addWeighted(frame,BV,cvLogo,BV2,0)
    cv2.imshow('Blended',Blended)
    cv2.moveWindow('Blended',780,300)

    FFG=cv2.bitwise_and(Blended,Blended,mask =FGMask)
    #cv2.imshow('FFG',FFG)
    #cv2.moveWindow('FFG',780,0)
    compFinal =cv2.add(BG,FFG)
    cv2.imshow('comFinal',compFinal)
    cv2.moveWindow('comFinal',780,0)
    
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
