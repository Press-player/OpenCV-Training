import cv2
dispW =960
dispH =720
flip =2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam =cv2.VideoCapture(camSet)

while True:
    ret,frame =cam.read()
#---------------Draw a Box------------------------
    frame =cv2.rectangle(frame,(0,100),(500,140),(255,0,0),-1)
#----------------Circle----------------------------------    
    frame =cv2.circle(frame,(500,500),200,(255,255,0),6)
#--------------Text--------------------------
    fnt =cv2.FONT_HERSHEY_DUPLEX
    frame =cv2.putText(frame,'My text',(200,200),fnt,2,(255,255,0),3)
#--------------Line--------------------------
    frame =cv2.line(frame,(0,0),(1000,1000),(0,255,0),6)  
#---------------ArrowewLine------------------------------------  
    frame =cv2.arrowedLine(frame,(0,700),(600,0),(0,255,0),6)    
#----------------------------------------------
    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()