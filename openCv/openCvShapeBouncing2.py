import cv2
dispW =960
dispH =720
flip =2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam =cv2.VideoCapture(camSet)
dispW =int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
dispH =int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
BW =int(.15*dispW)
BH =int(.15*dispH)
posY =10
posX =270
dX =5
dY =5
while True:
    ret,frame =cam.read()
#---------------Draw a Box------------------------
    cv2.moveWindow('piCam',0,0)
    frame =cv2.rectangle(frame,(posX,posY),(posX+BW,posY+BH),(255,0,0),-1)
    cv2.imshow('piCam',frame)
    posX =posX+dX
    posY =posY+dY
    if posX<=0 or posX+BW>=dispW:
        dX=dX*(-1)
    if posY<=0 or posY+BH>=dispH:
        dY=dY*(-1)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()