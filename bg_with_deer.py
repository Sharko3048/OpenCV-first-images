import cv2

deer=cv2.imread("opencv/TheDeer.webp",cv2.IMREAD_COLOR)

row,column=deer.shape[0:2]
print(row,column)
rotated=cv2.getRotationMatrix2D((row/2,column/2),45,1)
rotated_deer=cv2.warpAffine(deer,rotated,(row,column))

refl_bordered_deer=cv2.copyMakeBorder(rotated_deer,1000,1000,1000,1000,cv2.BORDER_REFLECT)

saved_ima=cv2.imwrite("bg_of_deer.webp",refl_bordered_deer)
print(saved_ima)
cv2.imshow("DEER",refl_bordered_deer)
cv2.waitKey(0)
cv2.destroyAllWindows()