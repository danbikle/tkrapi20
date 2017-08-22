"""
dev.py

This script should help me do development.

Demo:
. env.bash
$PYTHON dev.py
"""


import io
import pdb
import os
import flask
import datetime      as dt
import flask_restful as fr
import numpy         as np
import pandas        as pd
import sqlalchemy    as sql
import keras
# modules in the py folder:


import pgdb
import kerastkr
import sktkr

# https://keras.io/models/model/#methods
batch_size_i = 256 # Doc: Number of samples per gradient update.
epochs_i     = 1 # Doc: Number of epochs to train the model.

# I should create a simple model.

def learn_predict_keraslinear(tkr='ABC',yrs=20,mnth='2016-11', features='pct_lag1,slope4,moy'):
  """This function should use keras to learn, predict."""
  # I should get train, test data.
  # Also get copy of test data in a DataFrame for later reporting:
  xtrain_a, ytrain_a, xtest_a, out_df = pgdb.get_train_test(tkr,yrs,mnth,features)
  if ((xtrain_a.size == 0) or (ytrain_a.size == 0) or (xtest_a.size == 0)):
    return out_df # probably empty too.
  # Start using Keras here.
  kmodel     = keras.models.Sequential()
  # I should fit a Keras model to xtrain_a, ytrain_a
  features_l = features.split(',')
  features_i = len(features_l)
  kmodel.add(keras.layers.core.Dense(features_i, input_shape=(features_i,)))
  # https://keras.io/activations/
  kmodel.add(keras.layers.core.Activation('linear'))
  # I should have 1 linear-output:
  kmodel.add(keras.layers.core.Dense(1)) 
  kmodel.add(keras.layers.core.Activation('linear'))
  kmodel.compile(loss='mean_squared_error', optimizer='adam')
  kmodel.fit(xtrain_a,ytrain_a, batch_size=batch_size_i, epochs=epochs_i)
  pdb.set_trace()
  # I should save the model:
  # https://keras.io/getting-started/faq/#how-can-i-save-a-keras-model
  import tempfile
  with tempfile.NamedTemporaryFile() as fp:
    pdb.set_trace()
    kmodel.save(fp.name)
    fp.seek(0)
    somebytes = fp.read()
    print(len(somebytes))

    # Use the codecs module to encode
    import codecs
    base64_data = codecs.encode(somebytes, 'base64')
    print(base64_data[:99])

  # I should predict xtest_a then update out_df
  predictions_a           = np.round(kmodel.predict(xtest_a),3)
  # Done with Keras, I should pass along the predictions.
  predictions_l           = [p_f[0] for p_f in predictions_a] # I want a list
  out_df['prediction']    = predictions_l
  out_df['effectiveness'] = np.sign(out_df.pct_lead*out_df.prediction)*np.abs(out_df.pct_lead)
  out_df['accuracy']      = (1+np.sign(out_df.effectiveness))/2
  algo                    = 'keraslinear'
  pgdb.predictions2db(tkr,yrs,mnth,features,algo,out_df)
  # I should return a DataFrame useful for reporting on the predictions.
  return out_df

pdb.set_trace()
out_df = learn_predict_keraslinear()

# I should save it to file(s).

# I should use it to predict.

stophere

valid_s = set([1,2,3,4,5])

maybe_s = set([1,2,3,6,7,6,7])

inter_s = valid_s.intersection(maybe_s)

stophere


pdb.set_trace()
features = pgdb.getfeatures()
stophere

tkr='FB';yrs=6;features='pct_lag1,pct_lag2,pct_lag4,slope6,slope4,slope8,moy,dow'
hl = 1; neurons = 3
pdb.set_trace()
out_df = kerastkr.learn_predict_kerasnn_tkr(tkr,yrs,features,hl,neurons)
print(out_df)
stophere

tkr='FB';yrs=6;features='pct_lag1,pct_lag2,pct_lag4,slope6,slope4,slope8,moy,dow'
hl = 1; neurons = 3 ; yr = 2017
pdb.set_trace()
out_df = kerastkr.learn_predict_kerasnn_yr(tkr,yrs,yr,features,hl,neurons)
print(out_df)
stophere

tkr='FB';yrs=5;features='pct_lag1,pct_lag2,pct_lag4,slope6,slope4,slope8,moy,dow'
hl = 1; neurons = 3
pdb.set_trace()
out_df = kerastkr.learn_predict_kerasnn_tkr(tkr,yrs,features,hl,neurons)
print(out_df)
stophere

tkr='FB';yrs=5;features='pct_lag1,pct_lag2,pct_lag4,slope6,slope4,slope8,moy,dow'
pdb.set_trace()
out_df = kerastkr.learn_predict_keraslinear_tkr(tkr,yrs,features)
print(out_df)
stophere

tkr='FB';yrs=7;features='pct_lag1,pct_lag2,pct_lag4,slope6,slope4,slope8,moy,dow'
pdb.set_trace()
out_df = sktkr.learn_predict_sklinear_tkr(tkr,yrs,features)
print(out_df)
stophere

tkr='FB';yrs=20;mnth='2017-08';features='pct_lag1,slope4,moy'
pdb.set_trace()
out_df = sktkr.learn_predict_sklinear(tkr,yrs,mnth,features)
print(out_df)

stophere

tkr='FB';yrs=20;features='pct_lag1,pct_lag2';mnth = '2010-11'
tkr='FB';yrs=20;features='pct_lag1,pct_lag2';mnth = '2017-07'
pdb.set_trace()
xtrain_a, ytrain_a, xtest_a, out_df = pgdb.get_train_test(tkr,yrs,mnth,features)
print(out_df)

stophere

tkr='SPY';yrs=20;features='pct_lag1,pct_lag2,pct_lag4,slope6,slope4,slope8,moy,dow'
pdb.set_trace()
out_df = kerastkr.learn_predict_keraslinear_tkr(tkr,yrs,features)
print(out_df)

stophere

tkr='IBM';yrs=20;features='pct_lag1,slope4,moy'
pdb.set_trace()
out_df = sktkr.learn_predict_sklinear_tkr(tkr,yrs,features)
print(out_df)

stophere

tkr='ABC';yrs=20;mnth='2017-09';features='pct_lag1,slope4,moy';yr=2017
pdb.set_trace()
out_df = sktkr.learn_predict_sklinear_yr(tkr,yrs,yr,features)
print(out_df)

stophere
tkr='ABC';yrs=20;mnth='2017-09';features='pct_lag1,slope4,moy'
pdb.set_trace()
out_df = sktkr.learn_predict_sklinear(tkr,yrs,mnth,features)
print(out_df)

stophere

out_df = kerastkr.learn_predict_kerasnn_yr()#tkr,yrs,yr,features_s)
print(out_df)

stophere

# out_df = kerastkr.learn_predict_kerasnn()#tkr,yrs,mnth,features_s,hl_i,neurons_i)

stophere

predictions_df = flaskr.learn_predict_sklinear(tkr='ABC',yrs=20,mnth='2016-11', features='pct_lag1,slope4,moy')
pdb.set_trace()
predictions_df
tkr='ABC';yrs=20;mnth='2016-11';features='pct_lag1,slope4,moy'
algo = 'sklinear'; algo_params = 'None Needed'

# I should convert it to a string
csv0_s = predictions_df.to_csv(index=False,float_format='%.3f')
csv_s      = "'"+csv0_s+"'"
tkr_s      = "'"+tkr+"'"
mnth_s     = "'"+mnth+"'"
features_s = "'"+features+"'"
algo_s     = "'"+algo+"'"
algo_params_s = "'"+algo_params+"'"
yrs_s      = str(yrs)

# I should insert into the DB
db_s = os.environ['PGURL']
conn = sql.create_engine(db_s).connect()

sql_s  = "CREATE TABLE IF NOT EXISTS predictions(tkr VARCHAR, yrs INTEGER, mnth VARCHAR, features VARCHAR, algo VARCHAR, algo_params VARCHAR, csv TEXT)"
conn.execute(sql_s)
sql_s  = "INSERT INTO predictions(tkr,yrs,mnth,features,algo,algo_params,csv)VALUES("+tkr_s+","+yrs_s+","+mnth_s+","+features_s+","+algo_s+","+algo_params_s+","+csv_s+")"
conn.execute(sql_s)

stophere

# I should select a row from features table like this:
# select tkr from features where tkr = 'ABC';
pdb.set_trace()
tkr = 'ABC'
sql_s  = "SELECT csv FROM features WHERE tkr = %s LIMIT 1"
result = conn.execute(sql_s,[tkr])
if not result.rowcount:
  print("  return {'no': 'data found'}  ")
myrow  = [row for row in result][0]
feat_df = pd.read_csv(io.StringIO(myrow.csv))
feat_df.head()

"""
tp1 = flaskr.Tkrprices()
pdb.set_trace()
tp1.get()
"""


'bye'
