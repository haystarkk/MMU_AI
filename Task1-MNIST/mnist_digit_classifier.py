"""
Task 1: MNIST Dataset - Digit Classifier
This program downloads the MNIST dataset and trains a neural network to recognize digits 0-9
"""

import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns

# ==================== PART A: Download and Load MNIST Dataset ====================
print("=" * 60)
print("PART A: Downloading and Loading MNIST Dataset")
print("=" * 60)

# Download MNIST dataset
print("\n1. Downloading MNIST dataset...")
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

print(f"Training data shape: {x_train.shape}")
print(f"Training labels shape: {y_train.shape}")
print(f"Test data shape: {x_test.shape}")
print(f"Test labels shape: {y_test.shape}")

# Explore the dataset
print("\n2. Dataset Information:")
print(f"Number of training samples: {len(x_train)}")
print(f"Number of test samples: {len(x_test)}")
print(f"Image dimensions: {x_train[0].shape}")
print(f"Pixel value range: {x_train.min()} to {x_train.max()}")
print(f"Unique labels (digits): {np.unique(y_train)}")

# Display sample images
print("\n3. Displaying sample images...")
fig, axes = plt.subplots(2, 5, figsize=(12, 6))
for i, ax in enumerate(axes.flat):
    ax.imshow(x_train[i], cmap='gray')
    ax.set_title(f'Digit: {y_train[i]}')
    ax.axis('off')
plt.suptitle('Sample MNIST Digits', fontsize=16)
plt.tight_layout()
plt.savefig('sample_digits.png')
print("Sample digits saved as 'sample_digits.png'")
plt.show()

# Program to Distinguish Digits 0-9 
print("\n" + "=" * 60)
print("PART B: Training Model to Distinguish Digits 0-9")
print("=" * 60)

# Preprocessing the data
print("\n4. Preprocessing data...")
# Normalize pixel values to range [0, 1]
x_train_normalized = x_train.astype('float32') / 255.0
x_test_normalized = x_test.astype('float32') / 255.0

# Reshaping for neural network (add channel dimension)
x_train_reshaped = x_train_normalized.reshape(x_train_normalized.shape[0], 28, 28, 1)
x_test_reshaped = x_test_normalized.reshape(x_test_normalized.shape[0], 28, 28, 1)

# Converting labels to categorical (one-hot encoding)
y_train_categorical = keras.utils.to_categorical(y_train, 10)
y_test_categorical = keras.utils.to_categorical(y_test, 10)

print(f"Training data shape after preprocessing: {x_train_reshaped.shape}")
print(f"Training labels shape after one-hot encoding: {y_train_categorical.shape}")

# Building the neural network model
print("\n5. Building Neural Network Model...")
model = keras.Sequential([
    # Convolutional layer 1
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    
    # Convolutional layer 2
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    
    # Convolutional layer 3
    layers.Conv2D(64, (3, 3), activation='relu'),
    
    # Flatten and dense layers
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax')
])

# Displaying model architecture
model.summary()

# Compiling the model
print("\n6. Compiling Model...")
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Training the model
print("\n7. Training Model...")
history = model.fit(
    x_train_reshaped, y_train_categorical,
    epochs=10,
    batch_size=128,
    validation_split=0.1,
    verbose=1
)

# Evaluating the model
print("\n8. Evaluating Model on Test Data...")
test_loss, test_accuracy = model.evaluate(x_test_reshaped, y_test_categorical, verbose=0)
print(f"Test accuracy: {test_accuracy * 100:.2f}%")
print(f"Test loss: {test_loss:.4f}")

# Making predictions
print("\n9. Making Predictions...")
y_pred = model.predict(x_test_reshaped)
y_pred_classes = np.argmax(y_pred, axis=1)

# Generating classification report
print("\n10. Classification Report:")
print(classification_report(y_test, y_pred_classes, target_names=[str(i) for i in range(10)]))

# Generating confusion matrix
print("\n11. Generating Confusion Matrix...")
cm = confusion_matrix(y_test, y_pred_classes)
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix - MNIST Digit Classification')
plt.ylabel('True Label')
plt.xlabel('Predicted Label')
plt.savefig('confusion_matrix.png')
plt.show()

# Plot training history
print("\n12. Plotting Training History...")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

ax1.plot(history.history['accuracy'], label='Training Accuracy')
ax1.plot(history.history['val_accuracy'], label='Validation Accuracy')
ax1.set_title('Model Accuracy')
ax1.set_xlabel('Epoch')
ax1.set_ylabel('Accuracy')
ax1.legend()

ax2.plot(history.history['loss'], label='Training Loss')
ax2.plot(history.history['val_loss'], label='Validation Loss')
ax2.set_title('Model Loss')
ax2.set_xlabel('Epoch')
ax2.set_ylabel('Loss')
ax2.legend()

plt.tight_layout()
plt.savefig('training_history.png')
plt.show()

# Testing on custom predictions
print("\n13. Testing on specific test images...")
fig, axes = plt.subplots(2, 5, figsize=(12, 6))
for i, ax in enumerate(axes.flat):
    idx = np.random.randint(0, len(x_test))
    ax.imshow(x_test[idx], cmap='gray')
    true_label = y_test[idx]
    pred_label = y_pred_classes[idx]
    color = 'green' if true_label == pred_label else 'red'
    ax.set_title(f'True: {true_label}\nPred: {pred_label}', color=color)
    ax.axis('off')
plt.suptitle('Model Predictions on Test Images', fontsize=16)
plt.tight_layout()
plt.savefig('predictions_demo.png')
plt.show()

# Saving the model
print("\n14. Saving Model...")
model.save('mnist_digit_classifier.h5')
print("Model saved as 'mnist_digit_classifier.h5'")

print("\n" + "=" * 60)
print("TASK 1 COMPLETED SUCCESSFULLY!")
print("=" * 60)