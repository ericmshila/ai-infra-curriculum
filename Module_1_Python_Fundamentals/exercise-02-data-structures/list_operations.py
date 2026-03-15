# Create a script: list_operations.py

# Sample dataset: image file paths for training
training_images = [
    "img_0001.jpg",
    "img_0002.jpg",
    "img_0003.jpg",
    "img_0004.jpg",
    "img_0005.jpg"
]

# Print dataset information
print(f"Total training images: {len(training_images)}")
print(f"First image: {training_images[0]}")
print(f"Last image: {training_images[-1]}")

# Add new images
training_images.append("img_0006.jpg")
training_images.extend(["img_0007.jpg", "img_0008.jpg"])

# Added 10 images
training_images.extend(["img_0009.jpg","img_0010.jpg","img_0011.jpg",
                        "img_0012.jpg","img_0013.jpg","img_0014.jpg",
                        "img_0015.jpg","img_0016.jpg","img_0017.jpg",
                        "img_0018.jpg",])

print(f"After adding: {len(training_images)} images")

# Insert image at specific position
training_images.insert(0, "img_0000.jpg")
print(f"First image now: {training_images[0]}")

# Remove images
removed = training_images.pop()  # Remove last
print(f"Removed: {removed}")

training_images.remove("img_0000.jpg")  # Remove by value
print(f"Final count: {len(training_images)}")

# Check if image exists
if "img_0003.jpg" in training_images:
    index = training_images.index("img_0003.jpg")
    print(f"Found img_0003.jpg at index {index}")

# Slice operations (get batches)
batch_size = 4
batch_1 = training_images[0:batch_size]
batch_2 = training_images[batch_size:batch_size*2]
print(f"Batch 1: {batch_1}")
print(f"Batch 2: {batch_2}")

# Reverse and sort
training_images_sorted = sorted(training_images)
print(f"Sorted: {training_images_sorted}")

training_images_reversed = list(reversed(training_images))
print(f"Reversed: {training_images_reversed}")