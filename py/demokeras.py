"""
demokeras.py

This script should demo keras.

Demo:
~/anaconda3/bin/python demokeras.py
"""

import keras
import numpy as np
import pdb

x0_a = np.array([1.1, 2.2])
x_a  = np.array((0+x0_a, 1+x0_a, 2+x0_a, 3+x0_a, 4+x0_a))
y_a  = np.array((1.3,2.1,3.4,4.0,5.2)).reshape((-1,1))
print('x_a:')
print(x_a)
print('y_a:')
print(y_a)

# I should build a keras model.
kmodel     = keras.models.Sequential()
features_i = len(x_a[0])
kmodel.add(keras.layers.core.Dense(features_i, input_shape=(features_i,)))
# https://keras.io/activations/
kmodel.add(keras.layers.core.Activation('linear'))
# I should have 1 linear-output:
kmodel.add(keras.layers.core.Dense(1)) 
kmodel.add(keras.layers.core.Activation('linear'))
kmodel.compile(loss='mean_squared_error', optimizer='adam')
kmodel.fit(x_a,y_a, batch_size=1, epochs=4)

xtest_a       = np.array((2.4,3.6))
predictions_a = kmodel.predict(xtest_a)

print('predictions_a:')
print(predictions_a)

'bye'
