"""
kerastkr.py

This script should use keras to learn from stock market data.

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

# https://keras.io/models/model/#methods
batch_size_i = 256 # Doc: Number of samples per gradient update.
epochs_i     = 128 # Doc: Number of epochs to train the model.

def learn_predict_kerasnn(tkr       = 'IBM'
                          ,yrs      = 20        # years to train
                          ,mnth     = '2016-11' # Month to predict
                          ,features = 'pct_lag1,slope4,moy'
                          ,hl       = 2 # number of hidden layers
                          ,neurons  = 4 # neurons in each hl
                          ):
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
  # Activations should have 'Dropout' to reduce overfitting:
  kmodel.add(keras.layers.core.Dropout(0.1)) 
  # I should add hidden layers
  for l_i in range(hl):
    # I should create a hidden layer with neurons here
    kmodel.add(keras.layers.core.Dense(neurons))
    # linear-Activation is 1 choice of several here:
    kmodel.add(keras.layers.core.Activation('linear'))
    kmodel.add(keras.layers.core.Dropout(0.1))
  # Done with    hidden layers
  # I should have 1 linear-output:
  kmodel.add(keras.layers.core.Dense(1)) 
  kmodel.add(keras.layers.core.Activation('linear'))
  kmodel.compile(loss='mean_squared_error', optimizer='adam')
  # NN model should train using more epochs than plain Linear:
  epochs_nn_i = 8 * epochs_i
  kmodel.fit(xtrain_a,ytrain_a, batch_size=batch_size_i, epochs=epochs_nn_i)
  # I should predict xtest_a then update out_df
  predictions_a           = np.round(kmodel.predict(xtest_a),3)
  # Done with Keras, I should pass along the predictions.
  predictions_l           = [p_f[0] for p_f in predictions_a] # I want a list
  out_df['prediction']    = predictions_l
  out_df['effectiveness'] = np.sign(out_df.pct_lead*out_df.prediction)*np.abs(out_df.pct_lead)
  out_df['accuracy']      = (1+np.sign(out_df.effectiveness))/2
  algo                    = 'kerasnn'
  algo_params             = str([hl,neurons])
  # I should save my work to the db:
  pgdb.predictions2db(tkr,yrs,mnth,features,algo,out_df,kmodel,algo_params)
  # I should return a DataFrame useful for reporting on the predictions.
  return out_df

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
  # I should predict xtest_a then update out_df
  predictions_a           = np.round(kmodel.predict(xtest_a),3)
  # Done with Keras, I should pass along the predictions.
  predictions_l           = [p_f[0] for p_f in predictions_a] # I want a list
  out_df['prediction']    = predictions_l
  out_df['effectiveness'] = np.sign(out_df.pct_lead*out_df.prediction)*np.abs(out_df.pct_lead)
  out_df['accuracy']      = (1+np.sign(out_df.effectiveness))/2
  algo                    = 'keraslinear'
  # I should save my work to the db:
  pgdb.predictions2db(tkr,yrs,mnth,features,algo,out_df,kmodel)
  # I should return a DataFrame useful for reporting on the predictions.
  return out_df

def load_predict_keraslinear(tkr='FB',yrs=3,mnth='2017-08', features='pct_lag1,slope4,moy'):
  """This function should demo how to predict from a model in the db."""
  learn_predict_keraslinear(tkr,yrs,mnth,features) # Store a model in the db.
  # I should connect to the DB
  db_s = os.environ['PGURL']
  conn = sql.create_engine(db_s).connect()
  sql_s = '''SELECT tkr,yrs,mnth,features,algo,algo_params, kmodel_h5
    FROM predictions
    WHERE tkr      = %s 
    AND   yrs      = %s
    AND   mnth     = %s
    AND   features = %s
    LIMIT 1'''
  result = conn.execute(sql_s,[tkr,yrs,mnth,features])
  if not result.rowcount:
    return ['no result'] # Probably, a problem.
  myrow     = [row for row in result][0]
  kmodel_h5 = (bytes(myrow.kmodel_h5))
  with open('/tmp/kmodel2.h5','wb') as fh:
    fh.write(kmodel_h5)
  kmodel = keras.models.load_model('/tmp/kmodel2.h5')
  
  xtrain_a, ytrain_a, xtest_a, out_df = pgdb.get_train_test(tkr,yrs,mnth,features)
  if ((xtrain_a.size == 0) or (ytrain_a.size == 0) or (xtest_a.size == 0)):
    return out_df # probably empty too.
  # Start using Keras here.
  # I should predict xtest_a then update out_df
  predictions_a           = np.round(kmodel.predict(xtest_a),3)
  # Done with Keras, I should pass along the predictions.
  predictions_l           = [p_f[0] for p_f in predictions_a] # I want a list
  out_df['prediction']    = predictions_l
  out_df['effectiveness'] = np.sign(out_df.pct_lead*out_df.prediction)*np.abs(out_df.pct_lead)
  out_df['accuracy']      = (1+np.sign(out_df.effectiveness))/2
  algo                    = 'keraslinear'
  
  return out_df
  
def learn_predict_keraslinear_yr(tkr='ABC',yrs=20,yr=2016, features='pct_lag1,slope4,moy'):
  """This function should use keras to learn and predict for a year."""
  empty_df = pd.DataFrame()
  yr_l     = [empty_df, empty_df] # Ready for pd.concat()
  # I should rely on monthy predictions:
  for mnth_i in range(1,13):
    mnth_s = str(mnth_i).zfill(2)
    mnth   = str(yr)+'-'+mnth_s
    m_df   = learn_predict_keraslinear(tkr,yrs,mnth, features)
    yr_l.append(m_df)
  # I should gather the monthy predictions:
  yr_df = pd.concat(yr_l, ignore_index=True)
  return yr_df

def learn_predict_keraslinear_tkr(tkr='ABC',yrs=20, features='pct_lag1,slope4,moy'):
  """This function should use keras to learn and predict for a tkr."""
  # From db, I should get a list of all months for tkr:
  mnth_l = pgdb.getmonths4tkr(tkr,yrs)
  # I should rely on monthy predictions:
  empty_df = pd.DataFrame()
  tkr_l    = [empty_df, empty_df] # Ready for pd.concat()
  for mnth_s in mnth_l:
    m_df = learn_predict_keraslinear(tkr,yrs,mnth_s, features)
    tkr_l.append(m_df)
  # I should gather the monthy predictions:
  tkr_df = pd.concat(tkr_l, ignore_index=True)
  return tkr_df

def learn_predict_kerasnn_yr(tkr    = 'FB'
                          ,yrs      = 3    # Years to train
                          ,yr       = 2017 # Predict this year
                          ,features = 'pct_lag1,slope4,moy'
                          ,hl       = 2 # number of hidden layers
                          ,neurons  = 4 # neurons in each hl
                          ):
  """This function should use keras to learn and predict for a year."""
  empty_df = pd.DataFrame()
  yr_l     = [empty_df, empty_df] # Ready for pd.concat()
  # I should rely on monthy predictions:
  for mnth_i in range(1,13):
    mnth_s = str(mnth_i).zfill(2)
    mnth   = str(yr)+'-'+mnth_s
    m_df   = learn_predict_kerasnn(tkr,yrs,mnth, features,hl,neurons)
    yr_l.append(m_df)
  # I should gather the monthy predictions:
  yr_df = pd.concat(yr_l, ignore_index=True)
  return yr_df

def learn_predict_kerasnn_tkr(tkr   = 'FB' # Predict all years for this tkr.
                          ,yrs      = 3    # years to train
                          ,features = 'pct_lag1,slope4,moy'
                          ,hl       = 2 # number of hidden layers
                          ,neurons  = 4 # neurons in each hl
                          ):
  """This function should use keras to learn and predict for a tkr."""
  # From db, I should get a list of all months, and thus all years, for tkr:
  mnth_l = pgdb.getmonths4tkr(tkr,yrs)
  # I should rely on monthy predictions:
  empty_df = pd.DataFrame()
  tkr_l    = [empty_df, empty_df] # Ready for pd.concat()
  for mnth_s in mnth_l:
    m_df = learn_predict_kerasnn(tkr,yrs,mnth_s, features)
    tkr_l.append(m_df)
  # I should gather the monthy predictions:
  tkr_df = pd.concat(tkr_l, ignore_index=True)
  return tkr_df

'bye'
