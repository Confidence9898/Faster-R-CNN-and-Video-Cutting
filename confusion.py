import numpy as np
from sklearn.metrics import confusion_matrix

# Ground truth annotations (true labels)
true_labels = ["kicking", "peeking", "lockpicking", "shoulderslam"]

# Predicted labels
predicted_labels = ["kicking", "peeking", "lockpicking", "shoulderslam"]

# List of all classes in your dataset
class_labels = ["kicking", "peeking", "lockpicking", "shoulderslam"]

# Create a confusion matrix
confusion_mat = confusion_matrix(true_labels, predicted_labels, labels=class_labels)

# Print the confusion matrix
print("Confusion Matrix:")
print(confusion_mat)