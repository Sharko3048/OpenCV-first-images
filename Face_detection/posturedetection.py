import cv2
import mediapipe as mp
import numpy as np

cam=cv2.VideoCapture(0)
#initialize mediapipe objects
mp_pose=mp.solutions.pose
mp_draw=mp.solutions.drawing_utils
pose=mp_pose.Pose()
while cam.isOpened():
    ret,frame=cam.read()
    if not ret:
        break
    
        
