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
print(key_points)