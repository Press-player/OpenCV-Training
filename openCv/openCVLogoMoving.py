import cv2
import numpy as np

#------------------------------------Setup Variables-------------------------------------
dispW =720
dispH =480
flip =2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam =cv2.VideoCapture(camSet)
cv2.namedWindow('piCam')
#---------------------------------------------------------------------------------------------
def nothing(x):
    pass

cv2.createTrackbar('BlendedValue', 'piCam',0,100,nothing)

#___--------------Moving Box Variables-------------------------------

BW =180
BH =120
posY =0
posX =0
dX =4
dY =4
#-----------------------------------------------------------

pLogo =cv2.imread('pl.jpg')
pLogo =cv2.resize(pLogo,(180,120))
pLogoGray =cv2.cvtColor(pLogo,cv2.COLOR_BGR2GRAY)


cv2.imshow('p Logo Gray',pLogoGray)
cv2.moveWindow('p Logo Gray',800,0)

_,BGMask =cv2.threshold(pLogoGray,220,255,cv2.THRESH_BINARY)
cv2.imshow('BG Mask',BGMask)
cv2.moveWindow('BG Mask',800,200)

FGMask =cv2.bitwise_not(BGMask)
cv2.imshow('FG Mask',FGMask)
cv2.moveWindow('FG Mask',800,400)

FG =cv2.bitwise_and(pLogo,pLogo,mask =FGMask)
cv2.imshow('FG Original',FG)
cv2.moveWindow('FG Original',1000,0)


while True:
    ret,frame =cam.read()

 #   BG =cv2.bitwise_and(frame,frame,mask =BGMask)
    frameFake = frame[posY:posY+BH,posX:posX+BW].copy()
    FG1 =cv2.bitwise_and(frameFake,frameFake,mask =BGMask) 
    cv2.imshow('Mask1',FG1)
    cv2.moveWindow('Mask1',1000,200) 

    compImage =cv2.add(FG1,FG)
    cv2.imshow('BG/FG',compImage)
    cv2.moveWindow('BG/FG',1000,400)

    BV =cv2.getTrackbarPos('BlendedValue','piCam')/100
    BV2 =1-BV
    Blended =cv2.addWeighted(frameFake,BV,pLogo,BV2,0)
   

    FFG=cv2.bitwise_and(Blended,Blended,mask =FGMask)
    #cv2.imshow('FFG',FFG)
    #cv2.moveWindow('FFG',780,0)
    compFinal =cv2.add(frameFake,FFG)
    cv2.imshow('comFinal',compFinal)
    cv2.moveWindow('comFinal',800,600)


#------------------------Rectangle Moving Conditions-------------------------------------------
#   frame =cv2.rectangle(frame,(posX,posY),(posX+BW,posY+BH),(0,255,0),4)
    frame[posY:posY+BH,posX:posX+BW]=compFinal
    posX =posX+dX
    posY =posY+dY
    if posX<=0 or posX+BW>=dispW:
        dX=dX*(-1)
    if posY<=0 or posY+BH>=dispH:
        dY=dY*(-1)
#---------------------------------------------------------------------------------------



#------------------------Show Frames from PiCam------------------------------------------------------------

    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0)






    
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
