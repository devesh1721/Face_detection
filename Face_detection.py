import cv2
face=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("img-1.jpg")
img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face.detectMultiScale(img,1.1,4)
for (x,y,w,h) in faces:
       cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)    
cv2.imshow("FACE DETECTION",img)
cv2.waitKey()
