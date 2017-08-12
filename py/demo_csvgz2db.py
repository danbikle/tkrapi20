"""
demo_csvgz2db.py

This script should demo how to insert a csv.gz file into a table.

Demo:
~/anaconda3/bin/python demo_csvgz2db.py
"""

from sqlalchemy import create_engine

# I should connect to the DB
db_s = 'postgres://tkrapi:tkrapi@127.0.0.1/tkrapi'
conn = create_engine(db_s).connect()

sql_s = "drop table if exists tkrprices"
conn.execute(sql_s)
