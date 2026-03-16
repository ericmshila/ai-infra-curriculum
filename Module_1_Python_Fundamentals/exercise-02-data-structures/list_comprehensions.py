# Create a script: list_comprehensions.py

# Sample data: model training losses
losses = [2.5, 2.1, 1.8, 1.5, 1.3, 1.2, 1.1, 1.05, 1.02, 1.01]

# Square all losses
squared_losses = [loss ** 2 for loss in losses]
print(f"Squared losses: {squared_losses}")

# Filter losses below threshold
low_losses = [loss for loss in losses if loss < 1.5]
print(f"Losses below 1.5: {low_losses}")

# Transform and filter
normalized_losses = [(loss - min(losses)) / (max(losses) - min(losses))
                     for loss in losses if loss < 2.0]
print(f"Normalized losses: {normalized_losses}")

# Nested list comprehension: create batches
data_points = list(range(1, 21))  # 20 data points
batch_size = 5
batches = [data_points[i:i+batch_size]
           for i in range(0, len(data_points), batch_size)]
print(f"Batches: {batches}")

# Process image dimensions
image_sizes = [(224, 224), (256, 256), (512, 512), (1024, 1024)]
total_pixels = [width * height for width, height in image_sizes]
print(f"Total pixels: {total_pixels}")

# Create one-hot encoding
classes = ["cat", "dog", "bird", "fish"]
target_class = "dog"
one_hot = [1 if cls == target_class else 0 for cls in classes]
print(f"One-hot for '{target_class}': {one_hot}")

# Parse model filenames
model_files = [
    "model_v1_acc_0.85.h5",
    "model_v2_acc_0.92.h5",
    "model_v3_acc_0.88.h5"
]

# Extract accuracies
accuracies = [float(f.split("_acc_")[1].replace(".h5", ""))
              for f in model_files]
print(f"Accuracies: {accuracies}")


# Find best model
best_idx = accuracies.index(max(accuracies))
best_model = model_files[best_idx]
print(f"Best model: {best_model} (acc: {max(accuracies)})")



# Conditional list building
training_config = {
    "epochs": 100,
    "batch_size": 32,
    "learning_rate": 0.001,
    "use_gpu": True,
    "augmentation": True
}

enabled_features = [key for key, value in training_config.items()
                   if isinstance(value, bool) and value]
print(f"Enabled features: {enabled_features}")