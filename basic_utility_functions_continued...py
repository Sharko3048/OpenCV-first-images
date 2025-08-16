import cv2
import numpy as np

deer=cv2.imread("opencv/TheDeer.webp",cv2.IMREAD_COLOR)
cv2.imshow("DEER",deer)
cv2.waitKey(0)
cv2.destroyAllWindows()

#resizing
resized_deer=cv2.resize(deer,(700,50))
cv2.imshow("DEER",resized_deer)
cv2.waitKey(0)
cv2.destroyAllWindows()

#adding a border
bordered_deer=cv2.copyMakeBorder(deer,10,10,10,10,cv2.BORDER_CONSTANT,value=(255,0,0))
cv2.imshow("DEER",bordered_deer)
cv2.waitKey(0)
cv2.destroyAllWindows()

#reflecting border
refl_bordered_deer=cv2.copyMakeBorder(deer,100,100,100,100,cv2.BORDER_REFLECT)
cv2.imshow("DEER",refl_bordered_deer)
cv2.waitKey(0)
cv2.destroyAllWindows()

#rotation
row,column=deer.shape[0:2]
print(row,column)
rotated=cv2.getRotationMatrix2D((row/2,column/2),90,0.5)
rotated_deer=cv2.warpAffine(deer,rotated,(row,column))
cv2.imshow("DEER",rotated_deer)
cv2.waitKey(0)
cv2.destroyAllWindows()

#edge detection
ye=cv2.Canny(deer,100,250)
cv2.imshow("DEER",ye)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Coverting image from one colour frame to another
colour_converted=cv2.cvtColor(deer,cv2.COLOR_BGR2HSV)
cv2.imshow("DEER",colour_converted)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Erosion-need an image with a clear bg for it to work
sukuna=cv2.imread("opencv/sukuna.jpg",cv2.IMREAD_COLOR)
eroded_s=cv2.erode(sukuna,np.ones((8,8)))
cv2.imshow("sukuna",eroded_s)
cv2.waitKey(0)
cv2.destroyAllWindows()