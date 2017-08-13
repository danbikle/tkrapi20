"""
genf.py

This script should generate features from dates and prices.

Demo:
~/anaconda3/bin/python genf.py
"""

import io
import pdb
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
    # I should get csv_s
    csv_s = row.csv
    csv_s[:99]
    feat_df = pd.read_csv(io.StringIO(csv_s),names=('cdate','cp'))
    feat_df.head()
    pdb.set_trace()
    feat_df['pct_lead'] = 100.0*((feat_df.cp.shift(-1) - feat_df.cp) / feat_df.cp).fillna(0)
    print(row.tkr)
    
'bye'
