"""
demo_csvgz2db.py

This script should demo how to insert a csv.gz file into a table.

Demo:
~/anaconda3/bin/python demo_csvgz2db.py
"""
import pandas as pd
import pdb
from sqlalchemy import create_engine

# I should connect to the DB
db_s = 'postgres://tkrapi:tkrapi@127.0.0.1/tkrapi'
conn = create_engine(db_s).connect()

sql_s = "drop table if exists tkrprices"
conn.execute(sql_s)

sql_s = "create table tkrprices(tkr varchar,csv text)"
conn.execute(sql_s)

# I should read a small csv.gz file:

csv_df = pd.read_csv('/tmp/request_tkr/csv/FB.csv.gz')
tkrprices_df         = csv_df[['Date','Close']].sort_values(['Date'])
tkrprices_df.columns = ['cdate','cp']

# I should convert tkrprices_df into a CSV string:
csv0_s = tkrprices_df.to_csv(index=False, float_format='%.3f')
csv_s  = "'"+csv0_s+"'"

sql_s = "insert into tkrprices(tkr,csv)values('FB',"+csv_s+")"
conn.execute(sql_s)

sql_s = "select csv from tkrprices limit 1"
result = conn.execute(sql_s)
# print(result)

# <sqlalchemy.engine.result.ResultProxy object at 0x7fcbccdade80>

for row in result:
    print(row['csv'])
