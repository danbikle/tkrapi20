#!/bin/bash

# request_tkr.bash

# This script should call request_tkr.py
# which should help me collect prices into CSV files

SCRIPT=`realpath $0`
SCRIPTPATH=`dirname $SCRIPT`
PARPATH=${SCRIPTPATH}/..
PYPATH=${PARPATH}/py

cat ${PARPATH}/tkrs.txt|while read TKR
do
  python ${PYPATH}/request_tkr.py $TKR
done

exit
