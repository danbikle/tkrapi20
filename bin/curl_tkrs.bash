#!/bin/bash

# curl_tkrs.bash

# This script should loop through a text file full of tkrs and feed each to curl_tkr.bash

#cat ../tkrs.txt | while read TKR
cat ../tkrlist.txt | while read TKR
do
    ./curl_tkr.bash        $TKR
    ls -la  /tmp/curl_tkr/${TKR}.csv
    gzip -f /tmp/curl_tkr/${TKR}.csv
done

exit

./curl_tkr.bash AAPL
./curl_tkr.bash IBM
./curl_tkr.bash ^GSPC
./curl_tkr.bash ^RUT

exit
