"""
genf.py

This script should generate features from dates and prices.

Demo:
. env.bash
$PYTHON py/genf.py
"""

import io
import os
import pdb
import numpy      as np
import pandas     as pd
import sqlalchemy as sql

print('Busy generating features...')

# I should connect to the DB:
db_s = os.environ['PGURL']
conn = sql.create_engine(db_s).connect()

sql_s = "drop table if exists features"
conn.execute(sql_s)

sql_s = "create table features(tkr varchar, csv text)"
conn.execute(sql_s)

# I should loop through the tkrprices table:
sql_s   = "select tkr,csvh from tkrprices order by tkr"
sql_sql = sql.text(sql_s)
result  = conn.execute(sql_sql)
if not result.rowcount:
  sys.exit(1)
for row in result:
  print(row.tkr)
  # I should convert each row into a DataFrame so I can generate features:
  feat_df = pd.read_csv(io.StringIO(row.csvh),names=('cdate','cp'))
  # But first, I should calculate the dependent variable:
  feat_df['pct_lead'] = 100.0*((feat_df.cp.shift(-1) - feat_df.cp) / feat_df.cp).fillna(0)
  # Now, I should get 'lag' features from price:
  feat_df['pct_lag1'] = 100.0*((feat_df.cp - feat_df.cp.shift(1))/feat_df.cp.shift(1)).fillna(0)
  feat_df['pct_lag2'] = 100.0*((feat_df.cp - feat_df.cp.shift(2))/feat_df.cp.shift(2)).fillna(0)
  feat_df['pct_lag4'] = 100.0*((feat_df.cp - feat_df.cp.shift(4))/feat_df.cp.shift(4)).fillna(0)
  feat_df['pct_lag8'] = 100.0*((feat_df.cp - feat_df.cp.shift(8))/feat_df.cp.shift(8)).fillna(0)

  # Now, I should calculate 'slope' features from price:
  for slope_i in [3,4,5,6,7,8,9]:
    rollx          = feat_df.rolling(window=slope_i)
    col_s          = 'slope'+str(slope_i)
    slope_sr       = 100.0 * (rollx.mean().cp - rollx.mean().cp.shift(1))/rollx.mean().cp
    feat_df[col_s] = slope_sr
    
  # Now, I should calculate 'date' features from cdate:
  dt_sr = pd.to_datetime(feat_df.cdate)
  dow_l = [float(dt.strftime('%w' ))/100.0 for dt in dt_sr]
  moy_l = [float(dt.strftime('%-m'))/100.0 for dt in dt_sr]
  dom_l = [float(dt.strftime('%-d'))       for dt in dt_sr] # maybe use later
  wom_l = [round(dom/5)/100.0             for dom in dom_l] # maybe use later
  feat_df['dow'] = dow_l
  feat_df['moy'] = moy_l

  # debug
  feat_df.to_csv('/tmp/tmp.csv',index=False, float_format="%.3f")
  # debug
  # I should convert to String to move it towards the db:
  csv0_s = feat_df.to_csv(index=False,header=True,float_format='%.3f')
  csv_s  = "'"+csv0_s+"'"
  tkr_s  = "'"+row.tkr+"'"
  sql_s  = "insert into features(tkr,csv)values("+tkr_s+","+csv_s+")"
  conn.execute(sql_s)
# I should check:
# ../bin/psql.bash
# select       tkr  from features;
# select count(tkr) from features;
# select tkr,csv from features limit 1;

'bye'
