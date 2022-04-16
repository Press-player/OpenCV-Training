import cv2
dispW =960
dispH =720
flip =2
def nothing(x):
    pass
cv2.namedWindow('piCam')
cv2.createTrackbar('xVar','piCam',0,dispW,nothing)
cv2.createTrackbar('yVar','piCam',0,dispH,nothing)
cv2.createTrackbar('figureHeight','piCam',2,dispH,nothing)
cv2.createTrackbar('figureWidth','piCam',2,dispW,nothing)
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam =cv2.VideoCapture(camSet)
while True:
    ret,frame =cam.read()
    xVar =cv2.getTrackbarPos('xVar','piCam')
    yVar =cv2.getTrackbarPos('yVar','piCam')
    figureWidth =cv2.getTrackbarPos('figureWidth','piCam')
    figureHeight =cv2.getTrackbarPos('figureHeight','piCam')

    cv2.rectangle(frame,(100+xVar,100+yVar),(100+figureWidth+xVar,100+figureHeight+yVar),(255,0,0),3)

    cv2.moveWindow('piCam',0,0)
    cv2.imshow('piCam',frame)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()