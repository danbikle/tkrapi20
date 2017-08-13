#!/bin/bash

# request_tkr.bash

# This script should call request_tkr.py
# which should help me collect prices into CSV files

PYTHON=${HOME}/anaconda3/bin/python
SCRIPT=`realpath $0`
SCRIPTPATH=`dirname $SCRIPT`
PARPATH=${SCRIPTPATH}/..
PYPATH=${PARPATH}/py
OUTDIRC=${HOME}'/tkrcsv/history'

date
echo busy...
# cat ${PARPATH}/tkrlist.txt|while read TKR
# debug:
cat ${PARPATH}/tkrlist.txt|grep AA|while read TKR
do
    echo busy with                   $TKR
    $PYTHON ${PYPATH}/request_tkr.py $TKR
    # I should remove null-strings:
    sed -i '/null/d' ${OUTDIRC}/${TKR}.csv
done
date

#debug
exit
#debug

${SCRIPTPATH}/retry_request_tkr.bash
${SCRIPTPATH}/retry_request_tkr.bash
${SCRIPTPATH}/retry_request_tkr.bash
${SCRIPTPATH}/retry_request_tkr.bash

exit
