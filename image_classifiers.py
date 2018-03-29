# basic libs
import os.path
from keras.models import Sequential
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Convolution2D, MaxPooling2D, ZeroPadding2D, Conv2D
from keras import optimizers
from keras.models import model_from_json
from keras.utils.np_utils import to_categorical
import numpy as np
# To make sure results are reproducible
np.random.seed(0)
# your libs
from keras.models import load_model
# end of imports

def basic_cnn_model(img_width, img_height):
    """
    Tasks: 
        1. if model file exists, reload it
        2. if model file doesn't exist, create the model
    :param img_width: standard image width
    :param img_height: standard image height
    :return cnn model.
    """
    model = None
    # your implementation here
    input_shape = (img_width, img_height, 3)
    path = "trained_models/cnn_model.h5"

    model = Sequential()
    model.add(Conv2D(32, kernel_size=5, activation='relu', input_shape=input_shape))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(32, 5, activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(64, 5, activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(64, 5, activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # Classifier layer
    model.add(Flatten())
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(5, activation='softmax'))

    # Let's compile your model
    model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

    if(os.path.isfile(path)) :
    	# load weights into new model
    	model.load_weights(path)
    	print('Load Model Weights From File')


    # end of implementation
    return model
