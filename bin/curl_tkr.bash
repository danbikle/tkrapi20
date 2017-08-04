#!/bin/bash

# curl_tkr.bash

# This script should call curl and help me study the response.

# Note the user-agent arg.
# I need to pass a string; variable with string fails

TKR=IBM

rm -f /tmp/curl_tkr.bash.cookiejar.txt

/usr/bin/curl --verbose \
              --cookie-jar /tmp/curl_tkr.bash.cookiejar.txt \
              --user-agent 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36' \
              https://finance.yahoo.com/quote/${TKR} \
              > /tmp/tkr0.html \
              2> /tmp/s0.txt

sleep 1

/usr/bin/curl --verbose \
              --cookie     /tmp/curl_tkr.bash.cookiejar.txt \
              --cookie-jar /tmp/curl_tkr.bash.cookiejar.txt \
              --user-agent 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36' \
              https://finance.yahoo.com/quote/${TKR}/history?p=${TKR} \
              > /tmp/tkr1.html \
              2> /tmp/s1.txt

# In /tmp/tkr1.html I should see text like this near CrumbStore
# "CrumbStore":{"crumb":"z6M4ACgDGXK"}

# sed -n means ignore lines which do not match
# I should match text left of 'CrumbStore'
# I should match text right of '"}'
crum=`sed -n '/CrumbStore/s/^.*CrumbStore":{"crumb":"//p' /tmp/tkr1.html | sed -n '1s/"}.*//p'`
#sed -n '/CrumbStore/s/^.*CrumbStore":{"crumb":"//p' /tmp/tkr1.html|sed -n '1s/"}.*//p' > /tmp/c.txt

sleep 1

# https://query1.finance.yahoo.com/v7/finance/download/IBM?period1=-252432000&period2=1501743600&interval=1d&events=history&crumb=9cxzOy3G0UF

# https://query1.finance.yahoo.com/v7/finance/download/%5EGSPC?period1=-631123200&period2=1501743600&interval=1d&events=history&crumb=9cxzOy3G0UF

/usr/bin/curl --verbose \
              --cookie     /tmp/curl_tkr.bash.cookiejar.txt \
              --cookie-jar /tmp/curl_tkr.bash.cookiejar.txt \
              --user-agent 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36' \
              "https://query1.finance.yahoo.com/v7/finance/download/${TKR}?period1=-631123200&period2=1501743600&interval=1d&events=history&crumb=${crum}" \
              > /tmp/${TKR}.csv \
              2> /tmp/s2.txt

exit
