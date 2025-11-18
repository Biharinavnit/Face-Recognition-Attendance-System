# Face Recognition Attendance System

## 📌 Overview
This project is a **Face Recognition-based Attendance System** built using **Python**, **OpenCV**, and **face_recognition** library. It detects faces in real-time, recognizes registered users, and marks their attendance automatically.

## 🚀 Features
- Real-time face detection
- High-accuracy face recognition
- Automatic attendance logging with date & time
- Stores attendance in CSV format
- Simple and user-friendly interface

## 🛠️ Tech Stack
- **Python**
- **OpenCV** (cv2)
- **face_recognition** library
- **NumPy**

## 📂 Project Structure
```
Project Folder
│── images/                    # Folder for registered user images
│── main.py                    # Main script for running the attendance system
│── encode_faces.py            # Script to encode faces from images folder
│── attendance.csv             # Auto-generated attendance file
│── requirements.txt           # Required libraries
│── README.md                  # Project documentation
```

## 🧑‍💻 Installation
🧰 Step-by-Step to Run the Face Recognition Attendance System
1️⃣ Setup Project Folder

Create a new folder, e.g.:

C:\Projects\FaceRecognitionAttendance\


Then place these files inside:

collect_images.py
train.py
recognize_and_mark_attendance.py
haarcascade_frontalface_default.xml

2️⃣ Install Required Libraries

Open Command Prompt / Terminal inside that folder and run:

pip install opencv-python numpy pandas


If you get an error for cv2.face, install:

pip install opencv-contrib-python

3️⃣ Run Scripts Step by Step
Step 1 – Collect Images

Run:

python collect_images.py


Enter:

Student ID: 22
Student Name: Navnit


✅ Look at the camera — it will capture ~40 images.
Press q to stop once enough images are collected.

Step 2 – Train the Model

Run:

python train.py


This will create:

trainer/trainer.yml
trainer/labels.pickle

Step 3 – Recognize and Mark Attendance

Run:

python recognize_and_mark_attendance.py


It opens your webcam and recognizes faces in real-time.
If a student is recognized:

Green rectangle → recognized face

Red rectangle → unknown face

Attendance is saved in attendance.csv.

Press q to stop.

4️⃣ Verify Attendance

Open the file attendance.csv.
It should look like:

id,name,date,time
22,Navnit,2025-11-11,14:10:22

5️⃣ Troubleshooting Tips
Problem	Fix
cv2.face not found	Install opencv-contrib-python
Camera not opening	Change camera index → cv2.VideoCapture(1)
Faces not detected	Increase lighting or check haarcascade path
Model not recognizing	Collect more varied images (different angles)

## 📷 Sample Output Screenshot
<img width="1920" height="1080" alt="Screenshot (102)" src="https://github.com/user-attachments/assets/5a2aeaad-5152-49b8-b8d5-541b879af0af" />


## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

## 📜 License
This project is open-source and available under the **MIT License**.

---
👍 If you like this project, don't forget to star the repo on GitHub!
