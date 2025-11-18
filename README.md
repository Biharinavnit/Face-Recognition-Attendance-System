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
1. Clone the repository:
```
git clone https://github.com/your-username/your-repo-name.git
```
2. Navigate to the project folder:
```
cd your-repo-name
```
3. Install dependencies:
```
pip install -r requirements.txt
```

## ▶️ How to Use
### Step 1: Add Images
Place clear photos of users inside the **images/** folder. Filenames should represent user names.

### Step 2: Encode Faces
Run the following command:
```
python encode_faces.py
```

### Step 3: Start Attendance System
```
python main.py
```
The system will open your webcam and begin face recognition.

## 📊 Attendance Output
Attendance will be saved in **attendance.csv** with:
- Name
- Date
- Time

## 📷 Sample Output Screenshot
(Add your project screenshot here)

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

## 📜 License
This project is open-source and available under the **MIT License**.

---
👍 If you like this project, don't forget to star the repo on GitHub!
