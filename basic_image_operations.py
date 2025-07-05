import cv2
#displaying original image
maimage=cv2.imread("opencv/sukuna.jpg",cv2.IMREAD_COLOR)
print(maimage)
cv2.imshow("mawindow",maimage)
cv2.waitKey(0)
cv2.destroyAllWindows()

#displaying greyscale version of image
ma2image=cv2.imread("opencv/sukuna.jpg",cv2.IMREAD_GRAYSCALE)
print(ma2image)
cv2.imshow("ma2window",ma2image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#saving image
saved_ima=cv2.imwrite("Sukuna_greyscale.jpg",ma2image)
print(saved_ima)