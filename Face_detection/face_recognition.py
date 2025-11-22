import cv2
import os
import numpy as n

main_folder="/Users/Arora/Desktop/AOA-Jetlearn projects/opencv/Face_detection/faces"

namesxlabels={}
images=[]
labels=[]

id=0
width=100
height=130

for root,subfolders,files in os.walk(main_folder):
    for subfolder in subfolders:
        path=os.path.join(main_folder,subfolder)
        namesxlabels[id]=subfolder
        for file in os.listdir(path):
            image=cv2.imread(os.path.join(path,file),cv2.IMREAD_GRAYSCALE)
            images.append(image)
            labels.append(id)
        id+=1

    

print(namesxlabels)
print(labels)
images=n.array(images)
labels=n.array(labels)
model=cv2.face.LBPHFaceRecognizer_create()
model.train(images,labels)

vid=cv2.VideoCapture(0)
classifier=cv2.CascadeClassifier("/Users/Arora/Desktop/AOA-Jetlearn projects/opencv/Face_detection/haarcascade_frontalface_default.xml")

while True:
    success,ogframe=vid.read()
    if not success:
        continue
    frame=cv2.cvtColor(ogframe,cv2.COLOR_BGR2GRAY)
    faces=classifier.detectMultiScale(frame,1.2,4)
    print(faces)

    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),5)
        faceye=frame[y:y+h,x:x+w]
        faceye=cv2.resize(faceye,(width,height))

    cv2.imshow("Face",ogframe)
    key=cv2.waitKey(9)
    if key == 27:
        break
