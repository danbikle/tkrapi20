#!/bin/bash

# flaskr.bash

SCRIPT=`realpath $0`
SCRIPTPATH=`dirname $SCRIPT`

cd $SCRIPTPATH
. env.bash

# This script should start a Flask RESTful server.
$PYTHON flaskr.py

exit
