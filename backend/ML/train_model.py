from django.shortcuts import render
import string
import tensorflow as tf
import keras
import csv
import pandas
from sklearn import model_selection
from keras import layers, models, optimizers
import os
import json
from sklearn import preprocessing
import spacy
from keras.preprocessing import text, sequence
import numpy as np
import io

en_model = spacy.load('en_core_web_sm')
stopwords = en_model.Defaults.stop_words
def writefromCSVFile(stringName):
    returnArray = []
    with open(stringName) as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for row in csv_reader:
            returnArray.append(row)
    return returnArray

def removePunctuation(tweet):
    for char in string.punctuation:
        tweet = str(tweet).replace(char,' ')
    return(tweet)
def removeExtraSpaces(tweet):
	tweet = str(tweet).replace("  ", " ")
	return tweet

def preProcess(string_body):
  new_value = string_body
  new_value = new_value.lower()
  new_value = removePunctuation(new_value)
  new_value = removeExtraSpaces(new_value)
 #new_value = removeStopWords(new_value)

  return new_value;

def removeStopWords(string_body):
  new_value = string_body
  for words in stopwords:
    new_value = new_value.replace(words, '')
  return new_value

print("starting")
csv_data = writefromCSVFile('Cleaned_Depression_Vs_Suicide.csv')


trainDF = pandas.DataFrame()
points = (int)((len(csv_data)))
features = (len(csv_data[0]))

discrete = []
continous = []
trainDF = pandas.DataFrame()

labels = []
data = []

for point in range(points):
	if (len(csv_data[point]) > 0):
		if(len(csv_data[point]) > 1):
			data.append(preProcess(csv_data[point][0]))
			if (csv_data[point][1] == "SuicideWatch"):
				labels.append(1)
			else:
				labels.append(0)

trainDF['text'] = data
trainDF['label'] = labels
print(trainDF.head())

train_x, valid_x, train_y, valid_y = model_selection.train_test_split(trainDF['text'], trainDF['label'])

print("Len of train_x: " + str(len(train_x)))
print("Len of valid_x: " + str(len(valid_x)))

# create a tokenizer
token = text.Tokenizer()
token.fit_on_texts(trainDF['text'])
word_index = token.word_index

train_seq_x = sequence.pad_sequences(token.texts_to_sequences(train_x), maxlen=100)
valid_seq_x = sequence.pad_sequences(token.texts_to_sequences(valid_x), maxlen=100)

tokenizer_json = token.to_json()
with io.open('tokenizer.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(tokenizer_json, ensure_ascii=False))


# vocab_size = len(word_index) + 1
# model = keras.Sequential()
# model.add(keras.layers.Embedding(vocab_size, 16))
# model.add(keras.layers.GlobalAveragePooling1D())
# model.add(keras.layers.Dense(64, activation=tf.nn.relu))
# model.add(keras.layers.Dense(64, activation=tf.nn.relu))
# model.add(keras.layers.Dense(64, activation=tf.nn.relu))
# model.add(keras.layers.Dense(1, activation=tf.nn.sigmoid))

# print(type(train_seq_x[0]))
# print((train_y))
# print(type(valid_seq_x[0]))


# model.compile(optimizer='adam',
#               loss='binary_crossentropy',
#               metrics=['acc'])

# history = model.fit(train_seq_x,
#                     train_y,
#                     epochs=4,
#                     batch_size=512,
#                     validation_data=(valid_seq_x, valid_y),
#                     verbose=1)
# model.save('saved_model/Depression_vs_Suicide')