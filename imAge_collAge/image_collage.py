import cv2
import os

path="/Users/Arora/Desktop/AOA-Jetlearn projects/opencv/imAge_collAge/ImAgAs"
os.chdir(path)
images=[]

WIDTH=1200
HEIGHT=800
total_w=0
total_h=0

for file in os.listdir(path):
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".webp"):
        images.append(file)
        readimg=cv2.imread(os.path.join(path,file),cv2.IMREAD_COLOR)
        variable=readimg.shape
        total_w=total_w + variable[0]
        total_h=total_h + variable[1]

av_w=total_w//len(images)
av_h=total_h//len(images)

print(av_w,av_h)

collage="mafirstcollage.mov"
fourcc = cv2.VideoWriter_fourcc(*'avc1')
vidio=cv2.VideoWriter(os.path.join(path,collage),fourcc,1,(av_w,av_h))
if not vidio.isOpened():
    print("This video didnt open ggrgrggrgrgrr")

for file in images:
    print(path+file)
    readimg=cv2.imread(os.path.join(path,file),cv2.IMREAD_COLOR)
    resized=cv2.resize(readimg,(av_w,av_h))
    vidio.write(readimg)
    
