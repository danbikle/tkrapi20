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

def getfeatures():
  """This function should return a list of features."""
  sql_s  = "SELECT csv FROM features WHERE tkr = 'FB' LIMIT 1"
  result = conn.execute(sql_s)
  if not result.rowcount:
    return ['no features found'] # Probably, a problem.
  myrow     = [row for row in result][0]
  feat_df   = pd.read_csv(io.StringIO(myrow.csv))
  columns_l = feat_df.columns.tolist()
  # I should remove cdate, cp, pct_lead:
  return columns_l[3:]

def check_features(f_s):
  """This function should check validity of f_s."""
  valid_features = getfeatures() # Use later
  features_s     = f_s.replace("'","").replace('"','')
  return features_s

def tkrinfo(tkr):
  """This function should return info about a tkr."""
  feat_df             = getfeat(tkr)
  if feat_df.empty:
    return {'tkr': ('No info for: '+tkr)}
  observation_count_i = int(feat_df.cdate.size)
  maxdate_row = feat_df.loc[feat_df.cdate == feat_df.cdate.max()]
  return {
    'tkr':                 tkr
    ,'observation_count':  observation_count_i
    ,'years_observations': np.round(observation_count_i/252.0,1)
    ,'mindate':            feat_df.cdate.min()
    ,'maxdate':            feat_df.cdate.max()
    ,'maxdate_price':      maxdate_row.cp.tolist()[0]
  }

def get_train_test(tkr,yrs,mnth,features):
  """Using tkr,yrs,mnth,features, this function should get train,test numpy arrays."""
  xtrain_a = np.array(())
  ytrain_a = np.array(())
  xtest_a  = np.array(())
  out_df   = pd.DataFrame()
  feat_df  = getfeat(tkr)
  if (feat_df.empty):
    # I should return empty objects:
    return xtrain_a, ytrain_a, xtest_a, out_df
  # I should get the test data from feat_df:
  test_bool_sr = (feat_df.cdate.str[:7] == mnth)
  test_df      =  feat_df.loc[test_bool_sr] # should be about 21 rows
  if (test_df.empty):
    # I should return empty objects:
    return xtrain_a, ytrain_a, xtest_a, out_df
  # I should get the training data from feat_df:
  max_train_loc_i = -1 + test_df.index[0]
  min_train_loc_i = max_train_loc_i - yrs * 252
  if (min_train_loc_i < 10):
    # I should return empty objects:
    return xtrain_a, ytrain_a, xtest_a, out_df
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

def getmonths4tkr(tkr,yrs):
  """Should return a List of mnth-strings suitable for learning from yrs years."""
  # I should get feat_df for tkr:
  feat_df = getfeat(tkr)
  if (feat_df.empty):
    # I should return empty List:
    return []
  # I should get a series of month-strings from feat_df.cdate
  mnth_sr = feat_df.cdate.str[:7] # Like: 2010-07
  mnth_a  = mnth_sr.unique() # Actually just unique values.
  mnth_l  = sorted(mnth_a.tolist())
  start_i     = 2+yrs*12 # I should start learning 2 months after yrs years.
  shortmnth_l = mnth_l[start_i:] # Has enough history for learning.
  return shortmnth_l

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
