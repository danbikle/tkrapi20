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

def learn_predict_keraslinear(tkr='ABC',yrs=20,mnth='2016-11', features='pct_lag1,slope4,moy'):
  """This function should use keras to learn, predict."""
  xtrain_a, ytrain_a, xtest_a, out_df = pgdb.get_train_test(tkr,yrs,mnth,features)
  # I should fit a model to xtrain_a, ytrain_a
  pdb.set_trace()
  features_l = features.split(',')
  features_i = len(features_l)
  kmodel     = keras.models.Sequential()
  kmodel.add(keras.layers.core.Dense(features_i, input_shape=(features_i,)))
  kmodel.add(keras.layers.core.Activation('linear'))
  kmodel.add(keras.layers.core.Dense(1)) # because I have 1 linear-output
  
  kmodel.fit(xtrain_a,ytrain_a)
  # I should predict xtest_a then update out_df
  out_df['prediction']    = np.round(kmodel.predict(xtest_a),3).tolist()
  out_df['effectiveness'] = np.sign(out_df.pct_lead*out_df.prediction)*np.abs(out_df.pct_lead)
  out_df['accuracy']      = (1+np.sign(out_df.effectiveness))/2
  algo = 'keraslinear'
  pgdb.predictions2db(tkr,yrs,mnth,features,algo,out_df)
  return out_df
'bye'
