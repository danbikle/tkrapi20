#!/bin/bash

# retry_request_tkr.bash

# This script should loop through a folder full of CSV files and maybe feed some to request_tkr.bash

PYTHON=${HOME}/anaconda3/bin/python
SCRIPT=`realpath $0`
SCRIPTPATH=`dirname $SCRIPT`
PARPATH=${SCRIPTPATH}/..
PYPATH=${PARPATH}/py

# In bash how to loop through a folder of files?
for FN in /tmp/request_tkr/csv/*.csv.gz
do
    fsz_s=`ls -1s $FN | cut -c1-3`
    if [ "$fsz_s" = '4 /' ]
    then
	echo This file should be larger:
	ls -l $FN
	echo I should retry to request it:
	TKR=`basename $FN | sed 's/.csv.gz//'`
	$PYTHON ${PYPATH}/request_tkr.py    $TKR
        gzip -f       /tmp/request_tkr/csv/${TKR}.csv
        ls -la        /tmp/request_tkr/csv/${TKR}.csv.gz
    fi
done
    
exit
