
"""
Fake News Detection Model
This script builds and trains a deep learning model to classify news articles as real or fake.
Large csv and GloVe txt files weren't uploaded to GitHub due to size constraints
"""

# Libraries: numpy, pandas, scikit learn and tenserflow

import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


# Variables Setup
embedding_dim = 50
max_length = 54
padding_type = 'post'
trunc_type = 'post'
oov_tok = "<OOV>"
training_size = 3000
test_portion = 0.1



#  Importing the Dataset
data = pd.read_csv("fakenews/news.csv")
# print(data.head())


# Preprocessing Dataset
data = data.drop(["Unnamed: 0"], axis=1)
# print(data.head(5))


# Data Encoding
le = preprocessing.LabelEncoder()
le.fit(data['label'])
data['label'] = le.transform(data['label'])


# Tokenization and Padding
title = []
text = []
labels = []
for x in range(training_size):
    title.append(data['title'][x])
    text.append(data['text'][x])
    labels.append(data['label'][x])



# Combine title and text for each row
combined_text = [f"{t} {tx}" for t, tx in zip(title, text)]

# Create tokenizer and fit on combined text
tokenizer1 = Tokenizer(oov_token=oov_tok)
tokenizer1.fit_on_texts(combined_text)

word_index1 = tokenizer1.word_index
vocab_size1 = len(word_index1)

# Convert combined text to sequences and pad them
sequences1 = tokenizer1.texts_to_sequences(combined_text)
padded1 = pad_sequences(sequences1, maxlen=max_length, padding=padding_type, truncating=trunc_type)



# Splitting Data for Training and Testing
split = int(test_portion * training_size)
training_sequences1 = padded1[split:training_size]
test_sequences1 = padded1[0:split]
test_labels = labels[0:split]
training_labels = labels[split:training_size]

# Reshaping Data for LSTM
training_sequences1 = np.array(training_sequences1)
test_sequences1 = np.array(test_sequences1)


embedding_index = {}
with open('fakenews/glove.6B/glove.6B.50d.txt', 'r', encoding='utf-8') as f:
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        embedding_index[word] = coefs
        
embedding_matrix = np.zeros((vocab_size1 + 1, embedding_dim))

for word, i in word_index1.items():
    if i < vocab_size1:
        embedding_vector = embedding_index.get(word)
        if embedding_vector is not None:
            embedding_matrix[i] = embedding_vector
            
            
            
# TensorFlow embedding technique with Keras Embedding Layer to 
# map original input data into some set of real-valued dimensions.

# Embedding: The embedding layer uses pre-trained GloVe embeddings.
# Conv1D: A 1D convolutional layer to detect patterns in the text.
# LSTM(64): An LSTM layer to capture long-term dependencies in the data.


# Embedding Layer → You read each word and understand its meaning (word vectors).
# Conv1D Layer → You spot repeating phrases or suspicious patterns.
# MaxPooling → You focus only on the most important patterns.
# LSTM Layer → You consider the context of the whole sentence to understand meaning.
# Dense + Sigmoid → You make a final judgment: Fake or Real.


# Model Architecture
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size1 + 1, embedding_dim, input_length=max_length, 
                              weights=[embedding_matrix], trainable=False),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Conv1D(64, 5, activation='relu'),
    tf.keras.layers.MaxPooling1D(pool_size=4),
    tf.keras.layers.LSTM(64),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# print(model.summary())


# Train the model
history = model.fit(
    training_sequences1, 
    np.array(training_labels), 
    epochs=50, 
    validation_data=(test_sequences1, np.array(test_labels)), 
    verbose=2
)
model.save("fakenews/fakenews_model.h5")


# Example new article
new_title = "Karry to go to France"
new_text = "in gesture of sympathy"

# Combine title and text just like in training
new_combined = f"{new_title} {new_text}"

# Convert to sequence and pad
new_sequence = tokenizer1.texts_to_sequences([new_combined])
new_padded = pad_sequences(new_sequence, maxlen=max_length, padding=padding_type, truncating=trunc_type)

# Make prediction
prediction = model.predict(new_padded, verbose=0)[0][0]

if prediction >= 0.5:
    print("This news is Fake")
else:
    print("This news is Real")

print("Tokenized sequence:", new_padded)
print("Prediction probability:", prediction)
