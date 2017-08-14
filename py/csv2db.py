"""
csv2db.py

This script should insert csv.gz files into a table.

Demo:
~/anaconda3/bin/python csv2db.py
"""

import glob
import pdb
import os
import pandas as pd
from sqlalchemy import create_engine

# I should connect to the DB
db_s = os.environ['PGURL']

conn = create_engine(db_s).connect()

sql_s = "drop table if exists tkrprices"
conn.execute(sql_s)

sql_s = "create table tkrprices(tkr varchar, csvd text, csvh text, csvs text)"
conn.execute(sql_s)

# I should read csv files:
for csvf_s in sorted(glob.glob(os.environ['TKRCSVH']+'/AB*.csv')):
  # I should avoid files which are too small:
  sz_i = os.path.getsize(csvf_s)
  print(csvf_s, sz_i)
  if (sz_i > 140):
    tkr0_s = csvf_s.split('/')[-1].split('.')[0] # should be something like 'IBM'
    csv_df = pd.read_csv(csvf_s)
    # I should convert to String and pick only two columns:
    csv0_s = csv_df.to_csv(index=False,header=False,columns=('Date','Close'),float_format='%.3f')
    csvh_s  = "'"+csv0_s+"'"
    tkr_s   = "'"+tkr0_s+"'"
    csvfd_s = os.environ['TKRCSVD']+'/'+tkr0_s+'.csv'
    csvfs_s = os.environ['TKRCSVS']+'/'+tkr0_s+'.csv'
    csvd0_s = pd.read_csv(csvfd_s).sort_values('Date').to_csv(index=False,header=False)
    csvs0_s = pd.read_csv(csvfs_s).sort_values('Date').to_csv(index=False,header=False)
    csvd_s  = "'"+csvd0_s+"'"
    csvs_s  = "'"+csvs0_s+"'"
    sql_s   = "insert into tkrprices(tkr,csvd,csvh,csvs)values("+tkr_s+","+csvd_s+","+csvh_s+","+csvs_s+")"
    conn.execute(sql_s)

# I should check:
# sql_s = "select tkr, csvh from tkrprices limit 1"
# result = conn.execute(sql_s)
# 
# for row in result:
#     print(row['tkr'],row['csvh'].split(',')[-2:])

# ../bin/psql.bash
# select       tkr  from tkrprices;
# select count(tkr) from tkrprices;
# select csvh from tkrprices where tkr='SNAP';
# select substring(csvh from 0 for 144) from tkrprices where tkr='SNAP';
# select tkr, substring(csvh from 0 for 22) from tkrprices;
# select tkr, csvs from tkrprices WHERE tkr = 'AAPL';
# select tkr, csvd from tkrprices WHERE tkr = 'AAPL';
'bye'

