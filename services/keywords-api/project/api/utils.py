# services/users/project/api/utils.py


from functools import wraps

from flask import request, jsonify
#from keras.preprocessing.text import Tokenizer
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import load_model
from tensorflow.keras import utils
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from sklearn.preprocessing import LabelBinarizer, LabelEncoder
from nltk import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from nltk.stem import WordNetLemmatizer
import numpy as np
import re
import pathlib
import pandas as pd



pathModelTrainedCPUSampleSize60 =  "{}/Sources/keyword_model.h5".format(pathlib.Path(__file__).parent.absolute())
pathModelTrainedGPUSOneFeature = "{}/Sources/keyword_model_v1.h5".format(pathlib.Path(__file__).parent.absolute())
pathModelTrainedGPUSampleSize60 = "{}/Sources/keyword_model_cpu.h5".format(pathlib.Path(__file__).parent.absolute())
modelGpu = load_model(pathModelTrainedGPUSOneFeature)

train_path = "{}/Sources/normalized_train_20.csv".format(pathlib.Path(__file__).parent.absolute())
test_path = "{}/Sources/normalized_test_20.csv".format(pathlib.Path(__file__).parent.absolute())

train_data = pd.read_csv(train_path)
test_data = pd.read_csv(test_path)

df_all_rows = pd.concat([train_data, test_data], ignore_index=True)
df_all_rows = df_all_rows.dropna()


main_categories = df_all_rows.groupby('Label').size().sort_values(ascending=False)
filtered_data = df_all_rows[df_all_rows.Label.apply(lambda x: x in main_categories.index[:22])]
X = filtered_data["Keyword"]
Y = filtered_data["Label"]
labels = filtered_data["Label"].unique()
seed = 40
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=seed ,stratify=Y)

encoder = LabelEncoder()
encoder.fit(y_train)
y_train = encoder.transform(y_train)
y_test = encoder.transform(y_test)
text_labels = encoder.classes_
max_words = 6000
tokenize = Tokenizer(num_words=max_words, char_level=False)
tokenize.fit_on_texts(x_train)
tokenize.fit_on_texts(x_test)
def make_prediction_single(keyword):
    modelGpu = load_model(pathModelTrainedGPUSOneFeature)
    enconded_word = tokenize.texts_to_matrix([keyword])
    proba = modelGpu.predict(enconded_word)
    return proba




