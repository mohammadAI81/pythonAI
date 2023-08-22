import face_recognition
import cv2

print("Hello")
cascPath = 'haarcascade_frontalface_default.xml'
cap = cv2.VideoCapture(0)
FaceCascade = cv2.CascadeClassifier(cascPath)

while True:
    cheke, frame = cap.read()
    videos = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # videos white and black
    # videos = cv2.adaptiveThreshold(videos, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 19, 5)
    face = FaceCascade.detectMultiScale(videos, minNeighbors=10)



    for (x, y, h, w) in face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        cv2.circle(frame , (x + int(w/2)  , y + int(h/2)), int(h/2), (0, 255, 0), 3)
        if len(face) >= 1:
            NEW_cap = cv2.putText(frame, 'Mohammad', (x + int(w/2), y+h+20 + int(float((w/2)/150)) *2),  cv2.FONT_HERSHEY_COMPLEX, float((w/2)/150), (255, 255, 255), 0 )
    

    if len(face) == 0:
        NEW_cap = frame
    cv2.imshow('Mohammad',NEW_cap)
    key = cv2.waitKey(1)
    if key == ord('q') or 0xFF == ord('q'):
        break
    
print('End')
cap.release()
cv2.destroyAllWindows()

