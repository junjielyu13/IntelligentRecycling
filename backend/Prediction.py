import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf
import pathlib

from tensorflow import keras
from tensorflow.python.keras import layers
from tensorflow.python.keras.models import Sequential


class Prediction:
    def __init__(self):
        return

    def _train(self, epochs):
        history = self.model.fit(
            self.train_ds,
            validation_data=self.val_ds,
            epochs=epochs
        )

    def setDataSet(self, dir):
        self.data_dir = dir
        self.train_ds = tf.keras.utils.image_dataset_from_directory(
            self.data_dir,
            validation_split=0.2,
            subset="training",
            seed=123)
        self.val_ds = tf.keras.utils.image_dataset_from_directory(
            self.data_dir,
            validation_split=0.2,
            subset="validation",
            seed=123)
        self.class_names = self.train_ds.class_names

        AUTOTUNE = tf.data.AUTOTUNE

        self.train_ds = self.train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
        self.val_ds = self.val_ds.cache().prefetch(buffer_size=AUTOTUNE)

        normalization_layer = layers.Rescaling(1. / 255)

        normalized_ds = self.train_ds.map(lambda x, y: (normalization_layer(x), y))
        num_classes = len(self.class_names)

        self.model = Sequential([
            layers.Rescaling(1. / 255, input_shape=(256, 256, 3)),
            layers.Conv2D(16, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(32, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(64, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Flatten(),
            layers.Dense(128, activation='relu'),
            layers.Dense(num_classes)
        ])

        self.model.compile(optimizer='adam',
                      loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                      metrics=['accuracy'])

        self._train(10)



if __name__ == "__main__":
    prediction = Prediction()
    prediction.setDataSet("../dataset")
    print(prediction.class_names)
    prediction._train(10)
