# train.py
import cv2
import os
import numpy as np

dataset_dir = "dataset"
trainer_dir = "trainer"
if not os.path.exists(trainer_dir):
    os.makedirs(trainer_dir)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()

images = []
labels = []
label_map = {}  # map numeric label -> name (for future use)

def get_images_and_labels(dataset_path):
    image_paths = []
    for folder in os.listdir(dataset_path):
        folder_path = os.path.join(dataset_path, folder)
        if not os.path.isdir(folder_path):
            continue
        # folder name format: ID.Name
        try:
            id_str, name = folder.split('.', 1)
            id_num = int(id_str)
        except Exception as e:
            print(f"Skipping folder with unexpected name: {folder}")
            continue
        label_map[id_num] = name
        for img_name in os.listdir(folder_path):
            img_path = os.path.join(folder_path, img_name)
            image_paths.append((img_path, id_num))
    return image_paths

pairs = get_images_and_labels(dataset_dir)
for img_path, id_num in pairs:
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        continue
    # optionally detect face region again (already cropped but safe)
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)
    if len(faces) == 0:
        # use full image
        images.append(img)
        labels.append(id_num)
    else:
        x,y,w,h = faces[0]
        face = img[y:y+h, x:x+w]
        images.append(face)
        labels.append(id_num)

if len(images) == 0:
    print("No training images found. Run collect_images.py first.")
    exit(1)

print("Training LBPH recognizer on", len(images), "images...")
recognizer.train(images, np.array(labels))
model_path = os.path.join(trainer_dir, "trainer.yml")
recognizer.write(model_path)
print("Saved trained model to", model_path)

# Save label map for later use
import pickle
with open(os.path.join(trainer_dir, "labels.pickle"), "wb") as f:
    pickle.dump(label_map, f)
print("Saved label map to trainer/labels.pickle")
