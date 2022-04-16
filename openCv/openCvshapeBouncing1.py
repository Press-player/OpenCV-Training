import cv2
dispW =960
dispH =720
flip =2
upCorner =10
leftCorner =10
rigthCorner =940
downCorner =700
motionSpeedX =10
motionSpeedY =10
xCurrentPosition =0
yCurrentPosition =0


camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam =cv2.VideoCapture(camSet)

while True:
    ret,frame =cam.read()
#---------------Making a move--------------------------------------------
    xCurrentPosition =xCurrentPosition+motionSpeedX
    yCurrentPosition =yCurrentPosition+motionSpeedY

    xCurrentPosition2 =(xCurrentPosition+50)
    yCurrentPosition2 =(yCurrentPosition+100)
#---------------Bouncing Bounderies-----------------------------------------------    
    if xCurrentPosition2>=rigthCorner:
        motionSpeedX = -abs(motionSpeedX)
    if yCurrentPosition2>=downCorner:
        motionSpeedY = -abs(motionSpeedY)
    if xCurrentPosition<=leftCorner:
        motionSpeedX = abs(motionSpeedX)
    if yCurrentPosition<=upCorner:
        motionSpeedY = abs(motionSpeedY)
#---------------Draw a Box------------------------
    frame =cv2.rectangle(frame,(xCurrentPosition,yCurrentPosition),(xCurrentPosition2,yCurrentPosition2),(255,0,0),-1)

#----------------------------------------------
    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()