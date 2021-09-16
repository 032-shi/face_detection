import face_recognition
import cv2
image = face_recognition.load_image_file("1.jpg")
face_locations = face_recognition.face_locations(image)

for (top, right, bottom, left) in face_locations:
    cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imwrite("sample.jpg", image)