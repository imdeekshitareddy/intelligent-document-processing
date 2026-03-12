import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Bidirectional
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder


# Sample Data
sentences = [
    ["Agreement","between","ABC","Pvt","Ltd","and","John","Smith"],
    ["Signed","on","12","January","2025"],
    ["Amount","is","5000","USD"]
]

labels = [
    ["O","O","ORG","ORG","ORG","O","PERSON","PERSON"],
    ["O","O","DATE","DATE","DATE"],
    ["O","O","MONEY","MONEY"]
]


# Build vocabulary
words = list(set([w for s in sentences for w in s]))
word2idx = {w:i+1 for i,w in enumerate(words)}

# Encode words
X = [[word2idx[w] for w in s] for s in sentences]

# Label Encoding
label_encoder = LabelEncoder()
flat_labels = [l for s in labels for l in s]

label_encoder.fit(flat_labels)

y = [[label_encoder.transform([l])[0] for l in s] for s in labels]


# Padding
max_len = 10

X = pad_sequences(X, maxlen=max_len, padding='post')
y = pad_sequences(y, maxlen=max_len, padding='post')


# Model
model = Sequential()

model.add(Embedding(input_dim=len(word2idx)+1,
                    output_dim=32,
                    input_length=max_len))

model.add(Bidirectional(LSTM(32, return_sequences=True)))

model.add(Dense(len(label_encoder.classes_), activation='softmax'))


model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])


# Train
model.fit(X,y,epochs=20)


# Save model
model.save("ner_model.h5")

print("Model Trained Successfully")