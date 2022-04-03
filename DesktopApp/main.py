from browserControl import WebAccess
from time import sleep
from datetime import timedelta, datetime
import numpy as np
import cv2
timelimit = 0 # time in  minutes
future_time = 0
def checkTime():
    if datetime.now() > future_time:
        print("Time is up")
        return True

def main(NAME,LIMIT,PLATFORM):
    timelimit = float(LIMIT)
    future_time = datetime.now() + timedelta(minutes=timelimit)
    print(future_time)
    web = WebAccess() # inititalizing and opening the browser


def monitor_human():
    return_var = 0

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

    first_read = True

    cap = cv2.VideoCapture(0)
    ret,img = cap.read()

    while(ret):
        ret,img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.bilateralFilter(gray,5,1,1)
        
        def checkTime():
            if datetime.now() > future_time:
                print("Time is up")
                return True

        faces = face_cascade.detectMultiScale(gray, 1.3, 5,minSize=(200,200))
        if(len(faces)>0):
            for (x,y,w,h) in faces:
                img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),10)

                roi_face = gray[y:y+h,x:x+w]
                roi_face_clr = img[y:y+h,x:x+w]
                eyes = eye_cascade.detectMultiScale(img,1.3,5,minSize=(50,50))
                for (ex,ey,ew,eh) in eyes:
                    img=cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)

                if(len(eyes)>=2):
                    pass
                else:
                    return_var=1

        else:
            return_var=1
        return(return_var)



    if PLATFORM == "youtube":
        web.youtube(NAME)
    elif PLATFORM == "netflix":
        web.Netflix(NAME)

    web.enterFullScreen() # this is to enter full screen mode

    if(checkTime()): # call this with each frame to calculate the remaining time
        web.switchState() # this is to pause the video
    
