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
print(x_a)
print(y_a)

'bye'
