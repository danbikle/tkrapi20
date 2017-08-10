#!/bin/bash

# retry_curl_tkrs.bash

# This script should loop through a folder full of CSV files and maybe feed some to curl_tkr.bash

SCRIPT=`realpath $0`
SCRIPTPATH=`dirname $SCRIPT`
PARPATH=${SCRIPTPATH}/..

# In bash how to loop through a folder of files?
for FN in /tmp/curl_tkr/*.csv.gz
do
    fsz_s=`ls -1s $FN | cut -c1-3`
    if [ "$fsz_s" = '4 /' ]
    then
	echo This file should be larger:
	ls -l $FN
	echo I should retry to curl it:
	TKR=`basename $FN | sed 's/.csv.gz//'`
        ${SCRIPTPATH}/curl_tkr.bash $TKR
        gzip -f      /tmp/curl_tkr/${TKR}.csv
        ls -la       /tmp/curl_tkr/${TKR}.csv.gz
    fi
done
    
exit
