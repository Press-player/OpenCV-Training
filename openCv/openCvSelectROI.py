import cv2

evt =-1

#----------------------Screen and Setup Variables-----------------------
dispW =620
dispH =480
flip =2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam =cv2.VideoCapture(camSet)
cv2.namedWindow('frame')

#-----------------------------------------------------------

#--------------------------Mouse Events Capture----------------------------------------
def clickAndDrop(event,x,y,flags,params):
    global xButtonDown
    global xButtonUp
    global yButtonDown
    global yButtonUp
    global evt
   
    if event==cv2.EVENT_LBUTTONDOWN:
        print("Mouse event was: ",event)
        print("x: ",x," y: ",y)
        xButtonDown =x
        yButtonDown =y
        evt =event
    if  event==cv2.EVENT_LBUTTONUP:
        print("Mouse event is: ",event)
        print("x: ",x," y: ",y)
        xButtonUp =x
        yButtonUp =y
        evt =event
#--------------------------------------------------------------------------

cv2.setMouseCallback('frame',clickAndDrop)

while True:
    ret,frame =cam.read()
#-------------------------Making New Frame-------------------------------------   
    if evt==4:
        roi =frame[yButtonDown:yButtonUp,xButtonDown:xButtonUp].copy()
        cv2.moveWindow('ROI',700,0)
        roi =cv2.rectangle(roi,(0,0),(xButtonUp-xButtonDown,yButtonUp-yButtonDown),(255,0,255),4)
        frame =cv2.rectangle(frame,(xButtonDown,yButtonDown),(xButtonUp,yButtonUp),(255,0,255),4)
        cv2.imshow('ROI',roi)
#---------------------------------------------------------------------------------

#----------Set ubications------------------------------------------------------------]
 
    cv2.moveWindow('frame',0,0)
#--------------------------------------------------------------
#----------------Showing Windows---------------------------------------------------    

    cv2.imshow('frame',frame)
#-----------------------------------------------------------------------------------


    if cv2.waitKey(1)==ord('q'):
        break
#--------------------Clear---------------------------------------------------------------
cam.release()
cv2.destroyAllWindows()