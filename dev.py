"""
dev.py

This script should help me do development.

Demo:
. env.bash
$PYTHON dev.py
"""

import pdb
import os
import flask
import flask_restful as fr
import sqlalchemy as sql
import pandas as pd

import flaskr

# I should connect to the DB
db_s = os.environ['PGURL']
conn = sql.create_engine(db_s).connect()


"""
tp1 = flaskr.Tkrprices()
pdb.set_trace()
tp1.get()
"""


'bye'
