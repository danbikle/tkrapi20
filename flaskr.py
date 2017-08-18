"""
flaskr.py

Demo:
. env.bash
$PYTHON flaskr.py
Other shell:
curl localhost:5011/demo11.json
curl localhost:5011/static/hello.json
"""

import pgdb
import io
import pdb
import os
import flask
import datetime      as dt
import flask_restful as fr
import numpy         as np
import pandas        as pd
import sqlalchemy    as sql
import sklearn.linear_model as skl

# I should connect to the DB
db_s = os.environ['PGURL']
conn = sql.create_engine(db_s).connect()

# I should ready flask_restful:
application = flask.Flask(__name__)
api         = fr.Api(application)

# I should fill lists which users want frequently:
with open('years.txt') as fh:
  years_l = fh.read().split()
  
with open('tkrlist.txt') as fh:
  tkrlist_l = fh.read().split()
  
class Demo11(fr.Resource):
  """
  This class should be a simple syntax demo.
  """
  def get(self):
    my_k_s = 'hello'
    my_v_s = 'world'
    return {my_k_s: my_v_s}
api.add_resource(Demo11, '/demo11.json')

class Tkrlist(fr.Resource):
  """
  This class should list all the tkrs in tkrlist.txt
  """
  def get(self):
    return {'tkrlist': tkrlist_l}
api.add_resource(Tkrlist, '/tkrlist')

class Istkr(fr.Resource):
  """
  This class should answer True, False given a tkr.
  """
  def get(self, tkr):
    torf = tkr in tkrlist_l
    return {'istkr': torf}
api.add_resource(Istkr, '/istkr/<tkr>')

class Years(fr.Resource):
  """
  This class should list all the years in years.txt
  """
  def get(self):
    return {'years': years_l}
api.add_resource(Years, '/years')

class Tkrprices(fr.Resource):
  """
  This class should list prices for a tkr.
  """
  def get(self, tkr):
    # I should get csvh from tkrprices in db:
    sql_s       = '''select csvh from tkrprices
      where tkr = %s  LIMIT 1'''
    result      = conn.execute(sql_s,[tkr])
    if not result.rowcount:
      return {'no': 'data found'}  
    myrow       = [row for row in result][0]
    return {'tkrprices': myrow.csvh.split()}
api.add_resource(Tkrprices, '/tkrprices/<tkr>')

def get_train_test(tkr,yrs,mnth,features):
  """Using tkr,yrs,mnth,features, this function should get train,test numpy arrays."""
  feat_df = pgdb.getfeat(tkr)
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

  sql_s = '''CREATE TABLE IF NOT EXISTS
    predictions(
    tkr VARCHAR
    ,yrs INTEGER
    ,mnth VARCHAR
    ,features VARCHAR
    ,algo VARCHAR
    ,algo_params VARCHAR
    ,csv TEXT)'''
  conn.execute(sql_s)
  sql_s = '''INSERT INTO predictions(
    tkr,yrs,mnth,features,algo,algo_params,csv)VALUES(
    '''+tkr_s+","+yrs_s+","+mnth_s+","+features_s+","+algo_s+","+algo_params_s+","+csv_s+")"
  conn.execute(sql_s)
  return True

#   /sklinear/ABC/25/2016-11/'pctlag1,slope4,moy'

def learn_predict_sklinear(tkr='ABC',yrs=20,mnth='2016-11', features='pct_lag1,slope4,moy'):
  """This function should use sklearn to learn, predict."""
  linr_model = skl.LinearRegression()
  xtrain_a, ytrain_a, xtest_a, out_df = get_train_test(tkr,yrs,mnth,features)
  # I should fit a model to xtrain_a, ytrain_a
  linr_model.fit(xtrain_a,ytrain_a)
  # I should predict xtest_a then update out_df
  out_df['prediction']    = np.round(linr_model.predict(xtest_a),3).tolist()
  out_df['effectiveness'] = np.sign(out_df.pct_lead*out_df.prediction)*np.abs(out_df.pct_lead)
  out_df['accuracy']      = (1+np.sign(out_df.effectiveness))/2
  algo = 'sklinear'
  predictions2db(tkr,yrs,mnth,features,algo,out_df)
  return out_df

def get_out_l(out_df):
  """This function should convert out_df to a readable format when in JSON."""
  out_l = []
  for row in out_df.itertuples():
    row_d       = {
      'date,price':[row.cdate,row.cp]
      ,'pct_lead': row.pct_lead
      ,'prediction,effectiveness,accuracy':[row.prediction,row.effectiveness,row.accuracy]
    }
    out_l.append(row_d)
  return out_l

class Sklinear(fr.Resource):
  """
  This class should return predictions from sklearn.
  """
  def get(self, tkr,yrs,mnth,features):
    out_df = learn_predict_sklinear(tkr,yrs,mnth,features)
    out_l  = get_out_l(out_df)
    return {'predictions': out_l}
api.add_resource(Sklinear, '/sklinear/<tkr>/<int:yrs>/<mnth>/<features>')
  
if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  application.run(host='0.0.0.0', port=port)
'bye'
