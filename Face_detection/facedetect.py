import cv2
import os

#creating a folder using code
main_folder="/Users/Arora/Desktop/AOA-Jetlearn projects/opencv/Face_detection/faces"
person="amaya"
path=os.path.join(main_folder,person)
if not os.path.isdir(path):
    print("Success")
    os.makedirs(path)

width=100
height=130

vid=cv2.VideoCapture(0)

classifier=cv2.CascadeClassifier("/Users/Arora/Desktop/AOA-Jetlearn projects/opencv/Face_detection/haarcascade_frontalface_default.xml")


count=0
while count < 100:
    success,ogframe=vid.read()
    if not success:
        continue
    frame=cv2.cvtColor(ogframe,cv2.COLOR_BGR2GRAY)
    faces=classifier.detectMultiScale(frame,1.2,4)
    print(faces)
    
    for x,y,w,h in faces:
        cv2.rectangle(ogframe,(x,y),(x+w,y+h),(0,0,255),5)
        faceye=frame[y:y+h,x:x+w]
        faceye=cv2.resize(faceye,(width,height))
        cv2.imwrite(path+"/"+str(count)+".png",faceye)
        count+=1
    
    cv2.imshow("faces",ogframe)
    cv2.waitKey(20)









