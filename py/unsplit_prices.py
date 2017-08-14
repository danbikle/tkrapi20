"""
unsplit_prices.py

This script should create a column named uscp which I see as unsplit_prices.

Given a splitdate, this script should find all prices at and after the splitdate.
Then uscp should be cp * split_ratio.

Demo:
. env.bash
$PYTHON py/unsplit_prices.py
"""

import os
import pdb
import pandas     as pd
import sqlalchemy as sql
from   fractions import Fraction

# I should connect to the db.
db_s = os.environ['PGURL']
conn = sql.create_engine(db_s).connect()

'bye'
