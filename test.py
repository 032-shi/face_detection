import face_recognition
import cv2
image = face_recognition.load_image_file("1.jpg") #対象の画像ファイルを選択
face_locations = face_recognition.face_locations(image) #顔の位置座標を配列で取得

for (top, right, bottom, left) in face_locations: #顔の位置を枠線で囲う処理
    cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imwrite("sample.jpg", image) #顔の位置に枠線を描いた画像を保存する