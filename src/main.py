import tensorflow as tf
import neural_model as nm


#temp until model is fully trained
nm.train_model(save=True, epochs=30)

#create Neural Network model, load weights from local file
save_location = "..\\model_saves\\model"
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
model_seq.load_weights(save_location)


#find file to check

#output answer to web page