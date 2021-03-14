from keras import layers, models
import tensorflow as tf
import json
from tensorflow.python.keras.preprocessing.text import tokenizer_from_json

current_folder = 'saved_model/Depression_vs_Suicide/'
with open(current_folder + 'tokenizer.json') as f:
    data = json.load(f)
    tokenizer = tokenizer_from_json(data)

new_model = tf.keras.models.load_model(current_folder)