import os
import random
import shutil
import zipfile

print('Hello world')
# Define dataset paths
data_dir = "C://Users//user//Downloads//Unseen_data//chords"
output_dir = "C://Users//user//Desktop//Skule//Winter 2025//APS360//Split_Chords_Dataset3"  # Where to save the split data

# Check if data_dir exists
if not os.path.exists(data_dir):
    print(f"Error: The directory {data_dir} does not exist.")
else:
    print(f"The directory {data_dir} exists.")

# Define split ratios
train_ratio = 0.8
val_ratio = 0.1
test_ratio = 0.1

for split in ["train", "val", "test"]:
    os.makedirs(os.path.join(output_dir, split), exist_ok=True)

# Get all files and shuffle
file_paths = []
labels = []
class_file_counts = {}

for class_name in os.listdir(data_dir):
    class_path = os.path.join(data_dir, class_name)
    if os.path.isdir(class_path):  # Ensure it's a directory
        files = [os.path.join(class_path, f) for f in os.listdir(class_path) if f.endswith(('.wav', '.mp3', '.flac'))]
        file_paths.extend(files)
        labels.extend([class_name] * len(files))
        class_file_counts[class_name] = len(files)

# Print the number of files found
print(f"Found {len(file_paths)} files in {data_dir}")

wav_files = [f for f in file_paths if f.endswith('.wav')]
print(f"Found {len(wav_files)} .wav files in {data_dir}")


for class_name, count in class_file_counts.items():
    print(f"Class {class_name}: {count} files")

# Shuffle while maintaining order between files and labels
combined = list(zip(file_paths, labels))
random.shuffle(combined)
file_paths, labels = zip(*combined)

# Split dataset
total_files = len(file_paths)
train_end = int(total_files * train_ratio)
val_end = train_end + int(total_files * val_ratio)

train_files = file_paths[:train_end]
val_files = file_paths[train_end:val_end]
test_files = file_paths[val_end:]

def copy_files(file_list, split_name):
    split_counts = {}
    for file in file_list:
        class_name = os.path.basename(os.path.dirname(file))
        split_path = os.path.join(output_dir, split_name, class_name)
        os.makedirs(split_path, exist_ok=True)
        shutil.copy(file, split_path)
        if class_name not in split_counts:
            split_counts[class_name] = 0
        split_counts[class_name] += 1
    return split_counts

# Copy files to respective folders and get counts
train_counts = copy_files(train_files, "train")
val_counts = copy_files(val_files, "val")
test_counts = copy_files(test_files, "test")

print("Train split:")
for class_name, count in train_counts.items():
    print(f"Class {class_name}: {count} files")

print("Validation split:")
for class_name, count in val_counts.items():
    print(f"Class {class_name}: {count} files")

print("Test split:")
for class_name, count in test_counts.items():
    print(f"Class {class_name}: {count} files")

print("Dataset split complete!")