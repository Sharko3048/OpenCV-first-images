import cv2 as c
black=c.imread("opencv/black.png",c.IMREAD_COLOR)
white=c.imread("opencv/white.png",c.IMREAD_COLOR)
c.imshow("secondprojw",black)
c.imshow("secondprojw2",white)
c.waitKey(0)

#adding images
new_image=c.add(black,white)
c.imshow("new_imagee",new_image)
c.waitKey(0)
