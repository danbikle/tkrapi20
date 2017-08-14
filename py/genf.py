"""
genf.py

This script should generate features from dates and prices.

Demo:
~/anaconda3/bin/python genf.py
"""

import io
import pdb
import numpy      as np
import pandas     as pd
import sqlalchemy as sql

print('Busy generating features...')

# I should connect to the DB:
db_s = 'postgres://tkrapi:tkrapi@127.0.0.1/tkrapi'
conn = sql.create_engine(db_s).connect()

sql_s = "drop table if exists features"
conn.execute(sql_s)

sql_s = "create table features(tkr varchar, csv text)"
conn.execute(sql_s)

# I should loop through the tkrprices table:
sql_s   = "select tkr,csvh from tkrprices WHERE tkr like 'AA%' order by tkr"
sql_sql = sql.text(sql_s)
result  = conn.execute(sql_sql)
if not result.rowcount:
  sys.exit(1)
for row in result:
    print(row.tkr)
    # I should convert each row into a DataFrame so I can generate features:
    feat_df = pd.read_csv(io.StringIO(row.csvh),names=('cdate','cp'))
    # But first, I should get the dependent variable:
    feat_df['pct_lead'] = 100.0*((feat_df.cp.shift(-1) - feat_df.cp) / feat_df.cp).fillna(0)
    # Now, I should get features:
    feat_df['pct_lag1'] = 100.0*((feat_df.cp - feat_df.cp.shift(1))/feat_df.cp.shift(1)).fillna(0)
    feat_df['pct_lag2'] = 100.0*((feat_df.cp - feat_df.cp.shift(2))/feat_df.cp.shift(2)).fillna(0)
    feat_df['pct_lag4'] = 100.0*((feat_df.cp - feat_df.cp.shift(4))/feat_df.cp.shift(4)).fillna(0)
    feat_df['pct_lag8'] = 100.0*((feat_df.cp - feat_df.cp.shift(8))/feat_df.cp.shift(8)).fillna(0)
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
# select csv from features where tkr='FB';

'bye'
