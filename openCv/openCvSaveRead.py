import cv2
dispW =960
dispH =720
flip =2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam =cv2.VideoCapture(camSet)
#------------------Save Video-------------------------------------------------
#outVid =cv2.VideoWriter('videos/myCam.avi',cv2.VideoWriter_fourcc(*'XVID'),21,(dispW,dispH))
#-------------------Read Video------------------
cam =cv2.VideoCapture('videos/myCam.avi')
while True:
    ret,frame =cam.read()
    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0)
   # outVid.write(frame)
    if cv2.waitKey(48)==ord('q'):
        break
cam.release()
outVid.release()
cv2.destroyAllWindows()