import cv2
import numpy

# green=numpy.uint8([[[0,255,0]]])
# greeninhsv=cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
# print(greeninhsv)

vid=cv2.VideoCapture("/Users/Arora/Desktop/AOA-Jetlearn projects/opencv/Invisiblity_cloak/cloak_for_jl.mp4")
for i in range(60):
    success,bg=vid.read()
    if not success:
        print("failed")
        continue
    
lowerbound=numpy.array([155,40,40])
upperbound=numpy.array([180,255,255])

while vid.isOpened():
    success,frame=vid.read()
    if not success:
        break
    frame1=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #identifying red area
    mask1=cv2.inRange(frame1,lowerbound,upperbound)
    #refining image
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,numpy.ones((3,3),numpy.uint8),iterations=2)
    #identifying other area
    mask2=cv2.bitwise_not(mask1)
    result1=cv2.bitwise_and(bg,bg,mask=mask1)
    result2=cv2.bitwise_and(frame,frame,mask=mask2)
    output=cv2.add(result1,result2)
    output=cv2.rotate(output,cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imshow("ma vid",output)
    cv2.waitKey(10)
    
    

    



