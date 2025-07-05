import cv2 as c
chalet=c.imread("opencv/chalet.jpg",c.IMREAD_COLOR)
moon=c.imread("opencv/moooooon.jpg",c.IMREAD_COLOR)
c.imshow("secondprojw",chalet)
c.imshow("secondprojw2",moon)
c.waitKey(0)

#adding images
new_image=c.add(chalet,moon)
c.imshow("new_imagee",new_image)
c.waitKey(0)

#weighted_addition
wi=c.addWeighted(chalet,0.5,moon,2,0)
c.imshow("new_imagee3",wi)
c.waitKey(0)

#subtract
new_image4=c.subtract(chalet,moon)
c.imshow("new_imagee4",new_image4)
c.waitKey(0)