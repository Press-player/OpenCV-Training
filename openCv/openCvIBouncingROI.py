import cv2
#----------------------Screen Variables-----------------------
dispW =620
dispH =480
flip =2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam =cv2.VideoCapture(camSet)

#--------------------------------------------------------------

#___--------------Moving Box Variables-------------------------------
dispW =int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
dispH =int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
BW =int(.20*dispW)
BH =int(.20*dispH)
posY =10
posX =270
dX =2
dY =2
#-----------------------------------------------------------
while True:
    ret,frame =cam.read()
#-------------------------Making Gray Frame-------------------------------------   
    frameGray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    roi =frame[posY:posY+BH,posX:posX+BW].copy()
    frameGray =cv2.cvtColor(frameGray,cv2.COLOR_GRAY2BGR)
#---------------------------------------------------------------------------------
#------------------------Rectangle Moving Conditions-------------------------------------------
    frameGray =cv2.rectangle(frameGray,(posX,posY),(posX+BW,posY+BH),(0,255,0),4)
    frameGray[posY:posY+BH,posX:posX+BW]=roi
    posX =posX+dX
    posY =posY+dY
    if posX<=0 or posX+BW>=dispW:
        dX=dX*(-1)
    if posY<=0 or posY+BH>=dispH:
        dY=dY*(-1)
#---------------------------------------------------------------------------------------
#----------Set ubications------------------------------------------------------------]
    cv2.moveWindow('ROI',700,0)
    cv2.moveWindow('frameGray',0,0)
#--------------------------------------------------------------
#----------------Showing Windows---------------------------------------------------    
    cv2.imshow('ROI',roi)
    cv2.imshow('frameGray',frameGray)
#-----------------------------------------------------------------------------------
    if cv2.waitKey(1)==ord('q'):
        break
#--------------------Clear---------------------------------------------------------------
cam.release()
cv2.destroyAllWindows()
