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

pdb.set_trace()

flaskr.learn_predict(tkr='ABC',yrs=20,mnth='2016-11')
stophere

# I should connect to the DB
db_s = os.environ['PGURL']
conn = sql.create_engine(db_s).connect()

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
