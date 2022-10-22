import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np

def prediction(image_dir, im_size = 256, class_names=['amarillo', 'azul', 'marron', 'verde']):
    model = load_model('../../neuronal model dev/modelGOOD.h5')
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

if __name__ == "__main__":
    path = "prueba.png"
    im_dim = 224
    contenedor_value, accuracy = prediction(path, im_size = im_dim)
    print(
        "This image most likely belongs to {} with a {:.2f} percent confidence."
        .format(contenedor_value, accuracy)
    )
    ig = io.imread(path)
    plt.imshow(ig)
    plt.show()