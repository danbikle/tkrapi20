#!/bin/bash

# curl_tkrs.bash

# This script should loop through a text file full of tkrs and feed each to curl_tkr.bash

# cat ${PARPATH}/tkrlist.txt | while read TKR

SCRIPT=`realpath $0`
SCRIPTPATH=`dirname $SCRIPT`
PARPATH=${SCRIPTPATH}/..

cat ${PARPATH}/tkrs.txt | while read TKR
do
    ${SCRIPTPATH}/curl_tkr.bash $TKR
    gzip -f      /tmp/curl_tkr/${TKR}.csv
    ls -la       /tmp/curl_tkr/${TKR}.csv.gz
done

exit

./curl_tkr.bash AAPL
./curl_tkr.bash IBM
./curl_tkr.bash ^GSPC
./curl_tkr.bash ^RUT

exit
