import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('photo.jpg')
img = cv2.resize(img, (img.shape[1] // 7 ,img.shape[0] // 7))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
for x,y,w,h in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
    roi_color = img[y:y+h, x:x+w]
    roi_gray = gray[y:y+h, x:x+w]
cv2.imshow('Face detect', img)
cv2.waitKey(0)
cv2.destroyAllWindows ()