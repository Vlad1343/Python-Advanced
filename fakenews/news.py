# Libraries: numpy, pandas, scikit learn and tenserflow

import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from keras_preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences


embedding_dim = 50
max_length = 54
padding_type = 'post'
trunc_type = 'post'
oov_tok = "<OOV>"
training_size = 3000
test_portion = 0.1




data = pd.read_csv("fakenews/news.csv")
# print(data.head())

data = data.drop(["Unnamed: 0"], axis=1)
# print(data.head(5))

le = preprocessing.LabelEncoder()
le.fit(data['label'])
data['label'] = le.transform(data['label'])


title = []
text = []
labels = []
for x in range(training_size):
    title.append(data['title'][x])
    text.append(data['text'][x])
    labels.append(data['label'][x])

tokenizer1 = Tokenizer()
tokenizer1.fit_on_texts(title)
word_index1 = tokenizer1.word_index
vocab_size1 = len(word_index1)
sequences1 = tokenizer1.texts_to_sequences(title)
padded1 = pad_sequences(sequences1, padding=padding_type, truncating=trunc_type)

split = int(test_portion * training_size)
training_sequences1 = padded1[split:training_size]
test_sequences1 = padded1[0:split]
test_labels = labels[0:split]
training_labels = labels[split:training_size]

training_sequences1 = np.array(training_sequences1)
test_sequences1 = np.array(test_sequences1)

