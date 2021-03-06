import json
import os
import sys
from pprint import pprint


def get_imports():
    """
    Import the needed modules.
    
    Returns
    --------
    import_string : str(multiline)
        all required imports to run generated code.
    """
    try:
        return \
        """
# File generated by DLMML Parser
import sys
import os
import numpy
import pandas
from matplotlib import pyplot
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D, ZeroPadding2D, AveragePooling2D
from keras.layers import Dense
from keras.layers import Flatten, Dropout
from keras.layers import SimpleRNN, LSTM
from keras.optimizers import SGD, RMSprop, Adam, Adagrad, Adadelta
from keras.preprocessing.image import ImageDataGenerator
"""
    except Exception as e:
        print(e)
