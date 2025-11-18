# collect_images.py
import cv2
import os

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

cascade_path = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

dataset_dir = "dataset"
create_folder(dataset_dir)

# Input: student ID and name
student_id = input("Enter numeric student ID (e.g., 22): ").strip()
student_name = input("Enter student name (no spaces recommended): ").strip()
label_folder = f"{student_id}.{student_name}"
save_path = os.path.join(dataset_dir, label_folder)
create_folder(save_path)

cap = cv2.VideoCapture(0)
count = 0
print("Capturing images. Press 'q' to quit early.")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    for (x, y, w, h) in faces:
        face_img = gray[y:y+h, x:x+w]
        count += 1
        filename = os.path.join(save_path, f"{str(count)}.jpg")
        cv2.imwrite(filename, face_img)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 2)
        cv2.putText(frame, f"Image {count}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2)

    cv2.imshow("Collecting Images", frame)
    key = cv2.waitKey(1) & 0xFF
    # stop if q pressed or collected 40 images
    if key == ord('q') or count >= 40:
        break

print(f"Saved {count} images to {save_path}")
cap.release()
cv2.destroyAllWindows()
