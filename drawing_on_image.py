import cv2

lambo=cv2.imread("opencv/images_cuz_yas/lambo.jpg",cv2.IMREAD_COLOR)
cv2.imshow("lambo",lambo)
cv2.waitKey(0)
cv2.destroyAllWindows()

#drawing a line
cv2.line(lambo,(0,0),(250,250),(255,0,0),4)
cv2.imshow("lambo",lambo)
cv2.waitKey(0)
cv2.destroyAllWindows()

#drawing a rectangle
cv2.rectangle(lambo,(0,0),(250,250),(255,0,0),4)
cv2.imshow("lambo",lambo)
cv2.waitKey(0)
cv2.destroyAllWindows()

#filled rectangle
cv2.rectangle(lambo,(250,0),(500,250),(0,0,255),-4)
cv2.imshow("lambo",lambo)
cv2.waitKey(0)
cv2.destroyAllWindows()

#filled circle
cv2.circle(lambo,(0,0),125,(0,255,0),-4)
cv2.imshow("lambo",lambo)
cv2.waitKey(0)
cv2.destroyAllWindows()

#putting text
cv2.putText(lambo,"YASS QUEEN",(500,500),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,0),2)
cv2.imshow("lambo",lambo)
cv2.waitKey(0)
cv2.destroyAllWindows()
