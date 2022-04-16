import cv2
dispW =320
dispH =240
flip =2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam =cv2.VideoCapture(camSet)
while True:
    ret,frame =cam.read()
    #------------First Window------------------------
    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0)

    #------------Second Window--------------------
    gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('grayVideo',gray)
    cv2.moveWindow('grayVideo',400,0)
    #-------------Third Window------------------
    gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frameSmallGray =cv2.resize(gray,(160,120))
    cv2.imshow('grayVideo2',frameSmallGray)
    cv2.moveWindow('grayVideo2',400,300)
    #------------Fourth Window--------------------
    frameSmall =cv2.resize(frame,(160,120))
    cv2.imshow('piSmallCam',frameSmall)
    cv2.moveWindow('piSmallCam',0,300)
#----------Quit Cameras------------------
    if cv2.waitKey(1)==ord('q'):
        break
    #-----Clean------------------------------
cam.release()
cv2.destroyAllWindows()