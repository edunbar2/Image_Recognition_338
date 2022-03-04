# Sources: tensorflow.org used for dataset searching, loading and saving models after training,
# and loading datasets for training
# YouTube channel Edureka used for Neural Network information and training practices.
# Dataset being used:


import tensorflow as tf
from tensorflow.keras import layers, models, datasets
import numpy as np
import matplotlib.pyplot as plt


def train_model(save=False, epochs=10):
    save_location="..\\model_saves\\model"  # Currently, set for Windows machine. Change when put on linux server.
    batch_size = 32
    img_height = 180
    img_width = 180
    # directory should be replaced with the location of images to be used for training
    directory = "C:\\Users\\eric\\Desktop\\training\\animals\\raw-img"

    print(f"Directory path is: {directory}")

    # Gather images from directory for preprocessing
    # remove batch size for convolutional neural network
    train_ds = tf.keras.utils.image_dataset_from_directory(  # testing images
        directory,
        labels='inferred',
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size,
        shuffle=True).repeat()

    print(type(train_ds))
    validation_ds = tf.keras.utils.image_dataset_from_directory(  # validation images
        directory,
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size,
        shuffle=True).repeat()


    # Verify files are organized properly. Using RGB values
    for image_batch, labels_batch in train_ds:
        print(image_batch.shape)
        print(labels_batch.shape)
        break

    # Convert RGB values to 0,..,1 scale
    normalization_layer = tf.keras.layers.Rescaling(1. / 255)

    # normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))

    AUTOTUNE = tf.data.AUTOTUNE
    train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
    validation_ds = validation_ds.cache().prefetch(buffer_size=AUTOTUNE)

    # build and train model
    # Currently the Neural network is based on a Sequential model.
    # This is imperfect compared to the convolutional Neural Networking model and will be replaced.
    num_classes = 10  # change depending on dataset being used!

    model_seq = tf.keras.Sequential([tf.keras.layers.Rescaling(1. / 255),
                                     tf.keras.layers.Conv2D(32, 3, activation='relu'),
                                     tf.keras.layers.MaxPooling2D(),
                                     tf.keras.layers.Conv2D(32, 3, activation='relu'),
                                     tf.keras.layers.MaxPooling2D(),
                                     tf.keras.layers.Conv2D(32, 3, activation='relu'),
                                     tf.keras.layers.MaxPooling2D(),
                                     tf.keras.layers.Flatten(),
                                     tf.keras.layers.Dense(128, activation='relu'),
                                     tf.keras.layers.Dense(num_classes)
                                     ])

    model_seq.compile(
        optimizer='adam',
        loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=['accuracy'])

    model_seq.fit(
        train_ds,
        steps_per_epoch=2000,
        validation_data=validation_ds,
        validation_steps=800,
        epochs=epochs
    )