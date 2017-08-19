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
import flask_restful as fr
import sqlalchemy as sql
import pandas as pd

import flaskr

import pgdb
import kerastkr

pdb.set_trace()
out_df = kerastkr.learn_predict_kerasnn()#tkr,yrs,mnth,features_s,hl_i,neurons_i)

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
