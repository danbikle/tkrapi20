"""
csvgz2db.py

This script should insert csv.gz files into a table.

Demo:
~/anaconda3/bin/python csvgz2db.py
"""

import glob
import pdb
import os
import pandas as pd
from sqlalchemy import create_engine

# I should connect to the DB
db_s = 'postgres://tkrapi:tkrapi@127.0.0.1/tkrapi'
conn = create_engine(db_s).connect()

sql_s = "drop table if exists tkrprices"
conn.execute(sql_s)

sql_s = "create table tkrprices(tkr varchar, csv text)"
conn.execute(sql_s)

# I should read csv.gz files:
for csvf_s in glob.glob('/tmp/request_tkr/csv/*.csv.gz'):
  # I should avoid files which are too small:
  sz_i = os.path.getsize(csvf_s)
  print(csvf_s, sz_i)
  if (sz_i > 123):
    tkr0_s = csvf_s.split('/')[-1].split('.')[0] # should be something like 'IBM'
    csv_df = pd.read_csv(csvf_s)
    # I should convert to String and pick only two columns:
    csv0_s = csv_df.to_csv(index=False,header=False,columns=('Date','Close'),float_format='%.3f')
    csv_s  = "'"+csv0_s+"'"
    tkr_s  = "'"+tkr0_s+"'"
    sql_s  = "insert into tkrprices(tkr,csv)values("+tkr_s+","+csv_s+")"
    conn.execute(sql_s)

# I should check:
# sql_s = "select tkr, csv from tkrprices limit 1"
# result = conn.execute(sql_s)
# 
# for row in result:
#     print(row['tkr'],row['csv'].split(',')[-2:])

# ../bin/psql.bash
# select       tkr  from tkrprices;
# select count(tkr) from tkrprices;
# select csv from tkrprices where tkr='FB';

'bye'

