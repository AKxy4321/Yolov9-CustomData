import os
from sklearn.model_selection import train_test_split

name = 'yolov9'
dataset = os.path.join('.', 'datasets', f'{name}', 'train')
# Read images and annotations
images = [os.path.join(f"{dataset}/images", x) for x in os.listdir(f"{dataset}/images")]
annotations = [
    os.path.join(f"{dataset}/labels", x)
    for x in os.listdir(f"{dataset}/labels")
    if x[-3:] == "txt"
]

images.sort()
annotations.sort()

# Split the dataset into train-valid-test splits
train_images, val_images, train_annotations, val_annotations = train_test_split(
    images, annotations, test_size=0.3, random_state=1
)

val_images, test_images, val_annotations, test_annotations = train_test_split(
    images, annotations, test_size=0.1, random_state=1
)

import shutil

# Define directories for train, validation, and test splits
dataset = os.path.join('.', 'datasets', f'{name}_split')
train_dir = os.path.join(dataset, 'train')
val_dir = os.path.join(dataset, 'valid')
test_dir = os.path.join(dataset, 'test')

# Create directories if they don't exist
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Copy images and annotations to train directory
for image_path, annotation_path in zip(train_images, train_annotations):
    shutil.copy(image_path, train_dir)
    shutil.copy(annotation_path, train_dir)

# Copy images and annotations to validation directory
for image_path, annotation_path in zip(val_images, val_annotations):
    shutil.copy(image_path, val_dir)
    shutil.copy(annotation_path, val_dir)
    
for image_path, annotation_path in zip(test_images, test_annotations):
    shutil.copy(image_path, test_dir)
    shutil.copy(annotation_path, test_dir)
