import cv2

vid=cv2.VideoCapture("/Users/Arora/Desktop/AOA-Jetlearn projects/opencv/Car_detection/cars.mp4")
classifier=cv2.CascadeClassifier("/Users/Arora/Desktop/AOA-Jetlearn projects/opencv/Car_detection/cars.xml")


while vid.isOpened():
    success,ogframe=vid.read()
    if not success:
        continue
    frame=cv2.cvtColor(ogframe,cv2.COLOR_BGR2GRAY)
    cars=classifier.detectMultiScale(frame,1.2,2)
    print(cars)

    for x,y,w,h in cars:
        cv2.rectangle(ogframe,(x,y),(x+w,y+h),(0,255,0),4)
    
    cv2.imshow("CARS",ogframe)
    key=cv2.waitKey(1)
    if key==27:
        break
