"""
demokeras.py

This script should demo keras.

Demo:
. ../env.bash
~/anaconda3/bin/python demokeras.py
"""

import io
import keras
import pdb
import os
import numpy      as np
import sqlalchemy as sql

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
kmodel.fit(x_a,y_a, epochs=12)
xtest_a      = np.array([2.4,3.6]).reshape(1,2) # 1 row, 2 columns
prediction_a = kmodel.predict(xtest_a) # s.b. about 2.5

print('prediction_a:')
print( prediction_a)

# I should save the model:
kmodel.save('/tmp/kmodel.h5')

# I should create a new model from the h5-file:
kmodel2       = keras.models.load_model('/tmp/kmodel.h5')

# I should use it to predict again:
prediction2_a = kmodel2.predict(xtest_a) # s.b. about 2.5

print('prediction2_a:')
print( prediction2_a)

# I should save the model to the db:
db_s = os.environ['PGURL'] # from ../env.bash
conn = sql.create_engine(db_s).connect()

sql_s = 'drop table if exists demokeras'
conn.execute(sql_s)

sql_s = 'create table if not exists demokeras(kmodel bytea)'
conn.execute(sql_s)
"""
import h5py
kmodel3 = h5py.File('/tmp/kmodel.h5','r')

# I should use it to predict again:
prediction3_a = kmodel3.predict(xtest_a) # s.b. about 2.5

print('prediction3_a:')
print( prediction3_a)

"""


with open('/tmp/kmodel.h5','rb') as fh:
    # I should copy the file into the db
    kmodel3 = fh.read()

sql_s = 'insert into demokeras(kmodel)values( %s )'
conn.execute(sql_s,[kmodel3])

# select count(*) from demokeras;

sql_s  = 'select kmodel from demokeras limit 1'
result = conn.execute(sql_s)
myrow  = [row for row in result][0]
pdb.set_trace()
kmodel4 = bytes(myrow.kmodel)

"""
bfh = io.BytesIO(myrow.kmodel)
bfh = io.BytesIO(kmodel4)
"""

with open('/tmp/kmodel4.h5','wb') as fh:
    fh.write(kmodel4)

# I should create a new model from the h5-file:
kmodel5       = keras.models.load_model('/tmp/kmodel4.h5')

# I should use it to predict again:
prediction5_a = kmodel5.predict(xtest_a) # s.b. about 2.5

print('prediction5_a:')
print( prediction5_a)

'bye'
