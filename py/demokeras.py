"""
demokeras.py

This script should demo keras.

Demo:
~/anaconda3/bin/python demokeras.py
"""

import keras
import numpy as np
import pdb

x_a = np.array(
[[  1.1,  2.2]
 ,[ 2.1,  3.2]
 ,[ 3.1,  4.2]
 ,[ 4.1,  5.2]
 ,[ 5.1,  6.2]])

y_a = np.array(
[[  1.3]
 ,[ 2.1]
 ,[ 3.4]
 ,[ 4. ]
 ,[ 5.2]])
print('x_a:')
print(x_a)
print(x_a.shape)
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
kmodel.fit(x_a,y_a, epochs=512)
xtest_a      = np.array([2.4,3.6]).reshape(1,2) # 1 row, 2 columns
prediction_a = kmodel.predict(xtest_a) # s.b. about 2.5

print('prediction_a:')
print(prediction_a)

# I should save the model:

kmodel.save('/tmp/kmodel.h5')

# I should create a new model from the h5-file:

kmodel2 = keras.models.load_model('/tmp/kmodel.h5')

prediction2_a = kmodel2.predict(xtest_a) # s.b. about 2.5

print('prediction2_a:')
print(prediction2_a)


'bye'
