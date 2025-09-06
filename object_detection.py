import cv2
import numpy as np

eyes=cv2.imread("opencv/images_cuz_yas/imageee.jpg",cv2.IMREAD_COLOR)
greyscale_eyes=cv2.cvtColor(eyes,cv2.COLOR_BGR2GRAY)

#detecting circles
detected_circles=cv2.HoughCircles(greyscale_eyes,cv2.HOUGH_GRADIENT,1,10,param1=60,param2=34,minRadius=20,maxRadius=40)
print(detected_circles)

#if circles are detected we proceed
if detected_circles is not None:
    dc=np.uint(np.around(detected_circles))
    for xc,yc,r in dc[0]:
        cv2.circle(eyes,(xc,yc),r,(0,255,0),4)
        cv2.circle(eyes,(xc,yc),2,(0,0,255),4)
        cv2.imshow("eyes",eyes)
        cv2.waitKey(0)
        cv2.destroyAllWindows()