import cv2

evt =-1
goFlag =0

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
    global x1,x2,y1,y2
    global goFlag
   
    if event==cv2.EVENT_LBUTTONDOWN:
        print("Mouse event was: ",event)
        print("x: ",x," y: ",y)
        x1 =x
        y1 =y
        goFlag =0
    if  event==cv2.EVENT_LBUTTONUP:
        print("Mouse event is: ",event)
        print("x: ",x," y: ",y)
        x2 =x
        y2 =y
        goFlag =1
#--------------------------------------------------------------------------

cv2.setMouseCallback('frame',clickAndDrop)

while True:
    ret,frame =cam.read()
#-------------------------Making New Frame-------------------------------------   
    if goFlag==1:
        frame =cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,255),4)
        roi =frame[y1:y2,x1:x2]  #Not Copy
        cv2.moveWindow('ROI',700,0)
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