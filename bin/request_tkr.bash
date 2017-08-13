#!/bin/bash

# request_tkr.bash

# This script should call request_tkr.py
# which should help me collect prices into CSV files

PYTHON=${HOME}/anaconda3/bin/python
SCRIPT=`realpath $0`
SCRIPTPATH=`dirname $SCRIPT`
PARPATH=${SCRIPTPATH}/..
PYPATH=${PARPATH}/py

date
echo busy...
#cat ${PARPATH}/tkrs.txt|while read TKR
cat ${PARPATH}/tkrlist.txt|while read TKR
do
    echo busy with                   $TKR
    $PYTHON ${PYPATH}/request_tkr.py $TKR
    # I should remove null-strings:
    sed -i '/null/d' /tmp/request_tkr/csv/${TKR}.csv
    gzip -f          /tmp/request_tkr/csv/${TKR}.csv
    gzip -f         /tmp/request_tkr/html/${TKR}.html
done
date

${SCRIPTPATH}/retry_request_tkr.bash
${SCRIPTPATH}/retry_request_tkr.bash
${SCRIPTPATH}/retry_request_tkr.bash
${SCRIPTPATH}/retry_request_tkr.bash

exit
