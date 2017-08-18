"""
pgdb.py

This script should provide sytnax to connect flask-restful to a postgres db.

"""

import io
import pdb
import os
import datetime      as dt
import numpy         as np
import pandas        as pd
import sqlalchemy    as sql

# I should connect to the DB
db_s = os.environ['PGURL']
conn = sql.create_engine(db_s).connect()

def getfeat(tkr):
  """This function should return a DataFrame full of features for a tkr."""
  sql_s  = "SELECT csv FROM features WHERE tkr = %s LIMIT 1"
  result = conn.execute(sql_s,[tkr])
  if not result.rowcount:
    return pd.DataFrame() # empty DF offers consistent behavior to caller.
  myrow  = [row for row in result][0]
  feat_df = pd.read_csv(io.StringIO(myrow.csv))
  return feat_df

def get_train_test(tkr,yrs,mnth,features):
  """Using tkr,yrs,mnth,features, this function should get train,test numpy arrays."""
  feat_df = getfeat(tkr)
  if (feat_df.empty):
    return False # I should pass a signal that I have no data.
  # I should get the test data from feat_df:
  test_bool_sr = (feat_df.cdate.str[:7] == mnth)
  test_df      =  feat_df.loc[test_bool_sr] # should be about 21 rows
  # I should get the training data from feat_df:
  max_train_loc_i = -1 + test_df.index[0]
  min_train_loc_i = max_train_loc_i - yrs * 252
  if (min_train_loc_i < 10):
    min_train_loc_i = 10
  train_df = feat_df.loc[min_train_loc_i:max_train_loc_i]
  # I should train:
  features_l = features.split(',')
  xtrain_df  = train_df[features_l]
  xtrain_a   = np.array(xtrain_df)
  ytrain_a   = np.array(train_df)[:,2 ]
  xtest_df   = test_df[features_l]
  xtest_a    = np.array(xtest_df)
  out_df     = test_df.copy()[['cdate','cp','pct_lead']]
  return xtrain_a, ytrain_a, xtest_a, out_df

def predictions2db(tkr,yrs,mnth,features,algo,predictions_df,algo_params='None Needed'):
  # I should convert DF to a string
  csv0_s = predictions_df.to_csv(index=False,float_format='%.3f')
  csv_s         = "'"+csv0_s+"'"
  tkr_s         = "'"+tkr+"'"
  mnth_s        = "'"+mnth+"'"
  features_s    = "'"+features+"'"
  algo_s        = "'"+algo+"'"
  algo_params_s = "'"+algo_params+"'"
  yrs_s         = str(yrs)
  # I should move CREATE TABLE to an initialization script.
  # Running this statement frequently is inefficient:
  sql_s = '''CREATE TABLE IF NOT EXISTS
    predictions(
    tkr          VARCHAR
    ,yrs         INTEGER
    ,mnth        VARCHAR
    ,features    VARCHAR
    ,algo        VARCHAR
    ,algo_params VARCHAR
    ,csv TEXT)'''
  conn.execute(sql_s)
  # Perhaps eventually I should replace DELETE/INSERT wit UPSERT:
  sql_s = '''DELETE FROM predictions
    WHERE tkr         = %s
    AND   yrs         = %s
    AND   mnth        = %s
    AND   features    = %s
    AND   algo        = %s
    AND   algo_params = %s
    '''
  conn.execute(sql_s,[tkr,yrs,mnth,features,algo,algo_params])
  sql_s = '''INSERT INTO predictions(
    tkr,yrs,mnth,features,algo,algo_params,csv)VALUES(
    '''+tkr_s+","+yrs_s+","+mnth_s+","+features_s+","+algo_s+","+algo_params_s+","+csv_s+")"
  conn.execute(sql_s)
  return True

'bye'
