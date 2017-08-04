#!/bin/bash

# curl_tkr.bash

# This script should call curl and help me study the response.

# Note the user-agent arg.
# I need to pass a string; variable with string fails



/usr/bin/curl --verbose \
	      --user-agent 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36' \
	      https://finance.yahoo.com/quote/IBM \
	      > /tmp/tkr.html \
	      2> /tmp/s.txt

exit
