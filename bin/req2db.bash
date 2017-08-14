#!/bin/bash

# req2db.bash

# This script should request prices and then load them into db.

SCRIPT=`realpath $0`
SCRIPTPATH=`dirname $SCRIPT`
cd ${SCRIPTPATH}/../
. env.bash

# I should request prices:
${SCRIPTPATH}/request_tkr.bash
# I should load prices into db:
$PYTHON ${PYPATH}/csv2db.py

exit
