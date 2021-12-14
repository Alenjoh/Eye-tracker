import cv2
import numpy as np
import dlib
import pyautogui
import time
cap=cv2.VideoCapture(0)
import os
os.system("PythonBook.pdf")

detector=dlib.get_frontal_face_detector()
predictor=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
while True:
    _, frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces=detector(gray)
    width  = cap.get(3)  # float `width`
    height = cap.get(4)  # float `height
    a=180
    b=300
    
    
    print(width,height)
    for face in faces:
        x1=face.left()
        y1=face.top()
        x2=face.right()
        y2=face.bottom()
        cv2.rectangle(frame, (x1,y1),(x2,y2),(0,255,0),3)
        landmarks=predictor(gray,face)
        #for n in range(0,68):
        #cv2.circle(frame,(int(width/2),int(height/2)),4,(0,255,0),-1)    
        x=landmarks.part(30).x
        y=landmarks.part(30).y
        cv2.circle(frame,(int(width/2),a),4,(0,255,0),-1)
        cv2.circle(frame,(int(width/2),b),4,(0,255,0),-1)
        cv2.circle(frame,(x,y),4,(255,0,0),-1)
        if y<a:
       
            for s in range(20):
               pyautogui.scroll(50)
              # time.sleep(0.5)
        elif y>b:
             
            for s in range(20):
               pyautogui.scroll(-50)
               #time.sleep(0.5)
        else: 
            continue
           
        #cv2.circle(frame,(x,y),4,(255,0,0),-1)
    
    cv2.imshow("Frame",frame)
    
    key=cv2.waitKey(1)
    if key==27:
        break