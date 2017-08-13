#!/bin/bash

# req2db.bash

# This script should request prices and then load them into db.

PYTHON=${HOME}/anaconda3/bin/python
SCRIPT=`realpath $0`
SCRIPTPATH=`dirname $SCRIPT`
PARPATH=${SCRIPTPATH}/..
PYPATH=${PARPATH}/py

cd $PARPATH
# I should request prices:
${SCRIPTPATH}/request_tkr.bash
# I should load prices into db:
$PYTHON ${PYPATH}/csvgz2db.py

exit
