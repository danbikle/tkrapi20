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
                          ,yrs      = 20
                          ,mnth     = '2016-11'
                          ,features = 'pct_lag1,slope4,moy'
                          ,hl       = 2 # number of hidden layers
                          ,neurons  = 4 # neurons in each hl
                          ):
  """This function should use keras to learn, predict."""
  # I should get train, test data.
  # Also get copy of test data in a DataFrame for later reporting:
  xtrain_a, ytrain_a, xtest_a, out_df = pgdb.get_train_test(tkr,yrs,mnth,features)
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
  pgdb.predictions2db(tkr,yrs,mnth,features,algo,out_df,algo_params)
  # I should return a DataFrame useful for reporting on the predictions.
  return out_df

def learn_predict_keraslinear(tkr='ABC',yrs=20,mnth='2016-11', features='pct_lag1,slope4,moy'):
  """This function should use keras to learn, predict."""
  # I should get train, test data.
  # Also get copy of test data in a DataFrame for later reporting:
  xtrain_a, ytrain_a, xtest_a, out_df = pgdb.get_train_test(tkr,yrs,mnth,features)
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
  pgdb.predictions2db(tkr,yrs,mnth,features,algo,out_df)
  # I should return a DataFrame useful for reporting on the predictions.
  return out_df
'bye'