import cv2
import os

main_folder="/Users/Arora/Desktop/AOA-Jetlearn projects/opencv/Invisiblity_cloak/Face_detection/faces"
person="amaya"
path=os.path.join(main_folder,person)
if not os.path.isdir(path):
    print("Success")
    os.makedirs(path)








