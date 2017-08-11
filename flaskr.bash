#!/bin/bash

# flaskr.bash

PYTHON=${HOME}/anaconda3/bin/python
SCRIPT=`realpath $0`
SCRIPTPATH=`dirname $SCRIPT`

cd $SCRIPTPATH

# This script should start a Flask RESTful server.
export FLASK_DEBUG=1
export PORT=5011
$PYTHON flaskr.py

exit
