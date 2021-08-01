import cv2
import numpy as np
import dlib

img = cv2.imread('samantha.jpg')
img = cv2.resize(img,(0,0),None,0.9,0.9)
imgOriginal = img.copy()
# webcam = True
# cap = cv2.VideoCapture(1)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = detector(imgGray)


for face in faces:
    x1,y1 = face.left(),face.top()#landmarks
    x2,y2 = face.right(),face.bottom()#landmarks
    imgOriginal=cv2.rectangle(imgOriginal, (x1, y1), (x2, y2), (0, 255, 0), 2)
    landmark = predictor(imgGray,face)
    ##let us draw these landmarks on our image to know exact loactions of the facial features
    for n in range(68):#there are 68 diffrent landmarks 
        x = landmark.part(n).x
        y = landmark.part(n).y
        cv2.circle(imgOriginal,(x,y),5,(50,50,255),cv2.FILLED)
        cv2.putText(imgOriginal, str(n), (x,y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0,0,255),1)

    print("x1:",x1)
    print("y1:",y1)
    print("x2:",x2)
    print("y2:",y2)
cv2.imshow("Original:",imgOriginal)
cv2.waitKey(0)
    

