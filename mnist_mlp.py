from __future__ import print_function

import keras
import numpy as np
from keras.datasets import mnist
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
from keras.preprocessing import image

def load_keras_model():
    model = load_model("models")
    return model

def predict_number(model, img, width, height):
    test_img = image.img_to_array(img)
    test_img = test_img.astype("float32")
    test_img = test_img.reshape(width, height)
    test_img /= 255
    test_img = test_img.reshape(1, width * height)
    res = model.predict(test_img, batch_size=1)
    return np.argmax(res)
