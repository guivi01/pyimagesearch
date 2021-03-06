# -----------------------------
#   IMPORTS
# -----------------------------
# Import the necessary packages
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout


# -----------------------------
#   SUDOKU NETWORK CLASS
# -----------------------------
class SudokuNet:
    @staticmethod
    def build(width, height, depth, classes):
        # Initialize the model
        model = Sequential()
        inputShape = (height, width, depth)
        # First set of CONV => RELU => POOL Layers
        model.add(Conv2D(32, (5, 5), padding="same", input_shape=inputShape))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        # Second set of CONV => RELU => POOL Layers
        model.add(Conv2D(32, (3, 3), padding="same"))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        # First set of FC => RELU Layers
        model.add(Flatten())
        model.add(Dense(64))
        model.add(Activation("relu"))
        model.add(Dropout(0.5))
        # Second set of FC => RELU Layers
        model.add(Dense(64))
        model.add(Activation("relu"))
        model.add(Dropout(0.5))
        # Softmax Classifier
        model.add(Dense(classes))
        model.add(Activation("softmax"))
        # Return the constructed network architecture
        return model

