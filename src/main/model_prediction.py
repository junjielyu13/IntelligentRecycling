import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import os

def prediction(image_dir, im_size = 256, class_names=['amarillo', 'azul', 'marron', 'verde']):
    model = load_model("D:\GitHub\HackForGood_6p\src\main\model.h5")
    sunflower_path = image_dir

    img = tf.keras.utils.load_img(
        sunflower_path, target_size=(im_size, im_size)
    )
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batchN
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    return class_names[np.argmax(score)], 100 * np.max(score)


from skimage import io
import matplotlib.pylab as plt

# if __name__ == "__main__":
#     #print("D:\GitHub\HackForGood_6p\src\main\model.h5")
    
# path = 'C:/Users/Junjie_Li/Downloads/img_2669439960.jpg'
#     im_dim = 224
#     #contenedor_value, accuracy = 
#     # print(
#     #     "This image most likely belongs to {} with a {:.2f} percent confidence."
#     #     .format(contenedor_value, accuracy)
#     # )
#     # ig = io.imread(path)
#     # plt.imshow(ig)
#     # plt.show()

# print(prediction(path, im_size = 224)) #('amarillo', 89.77444171905518)