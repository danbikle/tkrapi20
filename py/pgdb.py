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
    return False
  myrow  = [row for row in result][0]
  feat_df = pd.read_csv(io.StringIO(myrow.csv))
  return feat_df

'bye'
