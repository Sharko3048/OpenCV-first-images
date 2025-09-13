import cv2
import numpy as np

blobs=cv2.imread("opencv/images_cuz_yas/blobs.jpg",cv2.IMREAD_COLOR)
params=cv2.SimpleBlobDetector_Params()
params.filterByArea=True
params.minArea=100
params.filterByCircularity=True
params.minCircularity=0.9
params.filterByConvexity=True
params.minConvexity=0.7
params.filterByInertia=True
params.minInertiaRatio=0.6
detector=cv2.SimpleBlobDetector_create(params)

key_points=detector.detect(blobs)
amountofcircs=len(key_points)
print(key_points)

final_imagee=cv2.drawKeypoints(blobs,key_points,np.zeros((1,1)),(0,255,0),cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)
cv2.putText(final_imagee,f"Amount of circles:{amountofcircs}",(10,620),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0))
cv2.imshow(".",final_imagee)
cv2.waitKey(0)
cv2.destroyAllWindows()
