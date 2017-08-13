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

# I should connect to the DB:
db_s = 'postgres://tkrapi:tkrapi@127.0.0.1/tkrapi'
conn = sql.create_engine(db_s).connect()

# I should loop through the tkrprices table:
sql_s   = "select tkr,csv from tkrprices WHERE tkr like 'AA%' order by tkr"
sql_sql = sql.text(sql_s)
result  = conn.execute(sql_sql)
if not result.rowcount:
  sys.exit(1)
for row in result:
    print(row.tkr)
    pdb.set_trace()
    'bye'
def nada():

    # I should convert each row into a DataFrame so I can generate features:
    feat_df = pd.read_csv(io.StringIO(row.csv),names=('cdate','cp'))
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
    
'bye'
