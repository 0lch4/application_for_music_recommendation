import json
import numpy as np
import tensorflow as tf

with open('wynik2.json') as f:
    data = json.load(f)

X = np.array([[data['tempo'], data['valence'], data['loudness'],
             data['energy'], data['time_signature']] for i in range(len(data))])
Y = X.copy()

min_vals = np.array([[data['tempo']-10, data['valence']-0.1, data['loudness']-1,
                    data['energy']-0.1, data['time_signature']] for i in range(len(data))])
max_vals = np.array([[data['tempo']+10, data['valence']+0.1, data['loudness']+1,
                    data['energy']+0.1, data['time_signature']] for i in range(len(data))])

a = 0
b = 1
min_vals += 0.001
max_vals -= 0.001
X_norm = ((X - min_vals) / (max_vals - min_vals)) * (b - a) + a

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(5,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(5, activation='linear')
])

model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(X_norm, Y, epochs=100, batch_size=16)
