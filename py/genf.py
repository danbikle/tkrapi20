"""
genf.py

This script should generate features from dates and prices.

Demo:
~/anaconda3/bin/python genf.py
"""

import pdb
import pandas as pd
from sqlalchemy import create_engine

# I should connect to the DB
db_s = 'postgres://tkrapi:tkrapi@127.0.0.1/tkrapi'
conn = create_engine(db_s).connect()

'bye'
