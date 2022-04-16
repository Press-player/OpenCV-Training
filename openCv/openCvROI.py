import cv2
dispW =620
dispH =480
flip =2


camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam =cv2.VideoCapture(camSet)


while True:
    ret,frame =cam.read()
    roi =frame[200:300,0:200].copy()
    roiGray =cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    roiGray =cv2.cvtColor(roiGray,cv2.COLOR_GRAY2BGR)

    frame[200:300,0:200]=roiGray

    cv2.moveWindow('ROI',700,0)
    cv2.moveWindow('ROIGray',1000,0)
    cv2.moveWindow('piCam',0,0)

    cv2.imshow('ROI',roi)
    cv2.imshow('piCam',frame)
    cv2.imshow('ROIGray',roiGray)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
