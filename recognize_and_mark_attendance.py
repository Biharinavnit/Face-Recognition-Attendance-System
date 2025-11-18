import cv2
import os
import pandas as pd
import datetime
import pickle

cascade_path = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

trainer_dir = "trainer"
model_path = os.path.join(trainer_dir, "trainer.yml")
labels_path = os.path.join(trainer_dir, "labels.pickle")

if not os.path.exists(model_path) or not os.path.exists(labels_path):
    print("Trained model or labels not found. Run train.py first.")
    exit(1)

# Use cv2.face.LBPHFaceRecognizer_create only if opencv-contrib-python is installed
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(model_path)

# Load label mapping
with open(labels_path, "rb") as f:
    label_map = pickle.load(f)  # maps id -> name

attendance_file = "attendance.csv"

# Load existing attendance or create new
if os.path.exists(attendance_file):
    df_att = pd.read_csv(attendance_file)
else:
    df_att = pd.DataFrame(columns=["id", "name", "date", "time"])

marked_ids = set(df_att['id'].astype(str).tolist())  # avoid re-marking same ID

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

print("Starting camera. Press 'q' to stop.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
        id_pred, conf = recognizer.predict(face)
        confidence_threshold = 70  # Lower = more strict, higher = more lenient

        if conf < confidence_threshold:
            name = label_map.get(id_pred, "Unknown")
            display_text = f"{name} ({id_pred})"
            id_str = str(id_pred)

            if id_str not in marked_ids:
                now = datetime.datetime.now()
                date_str = now.strftime("%Y-%m-%d")
                time_str = now.strftime("%H:%M:%S")

                # ✅ Replace append() with concat()
                new_entry = pd.DataFrame([{
                    "id": id_pred,
                    "name": name,
                    "date": date_str,
                    "time": time_str
                }])
                df_att = pd.concat([df_att, new_entry], ignore_index=True)
                df_att.to_csv(attendance_file, index=False)
                marked_ids.add(id_str)

                print(f"Marked attendance for {name} (id:{id_pred}) at {date_str} {time_str}")

            color = (0, 255, 0)
        else:
            display_text = "Unknown"
            color = (0, 0, 255)

        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, display_text, (x, y-10), font, 0.8, color, 2)

    cv2.imshow("Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Session ended. Attendance saved to", attendance_file)
