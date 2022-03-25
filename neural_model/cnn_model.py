import numpy as np
import matplotlib as plt
import tensorflow as tf
from tensorflow import keras
from keras import datasets, layers, models
from keras.preprocessing.image import image
from keras .preprocessing.image import ImageDataGenerator

directory = "C:\\Users\\eric\\Desktop\\training\\animals\\raw-img"
batch_size = 32
imgGen = ImageDataGenerator(rescale=1/255, validation_split=0.2)

train_ds = imgGen.flow_from_directory(directory, target_size=(256, 256), batch_size=batch_size, subset="training")
validation_ds = imgGen.flow_from_directory(directory, target_size=(256, 256), batch_size=batch_size, subset="validation")
print(type(train_ds))
#Convolutional Neural Network Model
# model_con = models.Sequential()
# model_con.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(180, 180, 3)))
# model_con.add(layers.MaxPooling2D((2, 2)))
# model_con.add(layers.Conv2D(64, (3, 3), activation='relu'))
# model_con.add(layers.MaxPooling2D((2, 2)))
# model_con.add(layers.Conv2D(64, (3, 3), activation='relu'))
# model_con.add(layers.Flatten())
# model_con.add(layers.Dense(64, activation='relu'))
# model_con.add(layers.Dense(10))
# model_con.summary()
#
# model_con.compile(
#     optimizer='adam',
#     loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
#     metrics=['accuracy'])
#
# history = model.fit(train_ds)