# Install dependencies
import matplotlib.pyplot as plt
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
# print(tf.__version__)
# !pip install tensorflow tensorflow-lite-support


# ---------------------------
# 1. Load Dataset
# ---------------------------

# Ensure your dataset is in the format:
# recyclables/
#     plastic/
#     paper/
#     metal/
#     glass/

train_dir = '/content/recyclables/train'
val_dir = '/content/recyclables/val'

img_size = (150, 150)
batch_size = 32

datagen = ImageDataGenerator(rescale=1/255)

train_data = datagen.flow_from_directory(
    train_dir,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='categorical'
)

val_data = datagen.flow_from_directory(
    val_dir,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='categorical'
)

# ---------------------------
# 2. Build Lightweight CNN Model
# ---------------------------
model = models.Sequential([
    layers.Conv2D(16, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    layers.MaxPooling2D(),
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(4, activation='softmax')  # 4 classes
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

# ---------------------------
# 3. Train Model
# ---------------------------
history = model.fit(
    train_data,
    validation_data=val_data,
    epochs=10
)

# Save model
model.save("recycle_model.h5")
