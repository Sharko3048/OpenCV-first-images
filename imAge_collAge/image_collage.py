import cv2
import os

path="/Users/Arora/AOA-Jetlearn projects/opencv/imAge_collAge/ImAgAs/"
os.chdir(path)
images=[]

for file in os.listdir(path):
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".webp"):
        images.append(file)

collage="mafirstcollage.avi"

vidio=cv2.VideoWriter(path+collage,0,1,(1600,1200))


for file in images:
    print(path+file)
    readimg=cv2.imread(path+file,cv2.IMREAD_COLOR)
    vidio.write(readimg)
    
