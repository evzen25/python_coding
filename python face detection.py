import cv2

cascade_path = "f:/IT/PYTHON/Python/exercises/Projects/Python Face detection/haarcascade_frontalface_default.xml"
image_path = "f:/IT/PYTHON/Python/exercises/Projects/Python Face detection/6.jpg"


face_cascade = cv2.CascadeClassifier(cascade_path)

img = cv2.imread(image_path)

if img is None:
    print(f"Could not read image: {image_path}")
    exit(1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()







