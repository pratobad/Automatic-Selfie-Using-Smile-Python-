import cv2
import datetime


cap = cv2.VideoCapture(1) 
face_cascade = cv2.CascadeClassifier('hearcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

while True:
     frame = cap.read()
     original_frame = copy.copy(frame)
     gray = cv2.cvtColor (frame, cv2.COLOR_BGR2GRAY)
     face = face_cascade.detectMultiScale(gray, 1.3, 5)
     for x, y, w, h in face:
         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
         face_roi = frame[y:y+h, x:x+w]
         gray_roi= gray[y:y+h, x:x+w]
         smile = smile_cascade.detectMultiScale(gray_roi, 1.3, 25)
         for x1, y1, w1, h1 in smile:
             cv2.rectangle(face.roi, (x1, y1), (x1+w1, y1+h1), (0, 0, 255), 2)         
             time_stamp= datetime.datetime.nov().strftime('%Y-%m-%d-%H-%N-%S') 
             file_name = f'selfie-[time_stamp).png'
             cv2.imvrite(file_name, original_frame)

     cv2.imshow('can star', frame)
     if cv2.waitKey(10) == ord('q'):
        break
