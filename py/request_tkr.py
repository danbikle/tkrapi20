"""
request_tkr.py

This script should get price data.
Ref:
https://stackoverflow.com/questions/21736970/using-requests-module-how-to-handle-set-cookie-in-request-response
"""

import datetime
import os
import re
import requests
import pdb

# I should ensure the output folders exist
outdirh = '/tmp/request_tkr/html/'
outdirc = '/tmp/request_tkr/csv/'
os.system('mkdir -p '+outdirh+' '+outdirc)

# I should prepare to talk to Yahoo:
tkr          = '^GSPC'
user_agent_s = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
url_s        = 'https://finance.yahoo.com/quote/'+tkr+'/history?p='+tkr
headers_d    = {'User-Agent': user_agent_s}

with requests.Session() as ssn:
    tkr_r  = ssn.get(url_s)
    html_s = tkr_r.content.decode("utf-8")
    # debug
    with open(outdirh+tkr+'.html','w') as fh:
        fh.write(html_s)
    # debug
    # I should extract the value of crumb from a string like this:
    # lhs_html_s+'"CrumbStore":{"crumb":"z6M4ACgDGXK"}'+rhs_html_s
    # Here is how I do it with sed:
    # crum=`sed -n '/CrumbStore/s/^.*CrumbStore":{"crumb":"//p' /tmp/tkr1.html | sed -n '1s/"}.*//p'`
    # The above sed syntax cuts /tmp/tkr1.html into 3 pieces.
    # The crumb I want is in the middle piece.
    
    # Here is a different approach with Python.
    # I should create a regexp with 2-groups.
    # I should find crumb_s in the 2nd group.
    # This is a bit different than how I used sed which cut the string into 3 pieces instead of 2:
    pattern_re = r'(CrumbStore":{"crumb":")(.+?")'
    pattern_ma = re.search(pattern_re, html_s)
    crumb_s    = pattern_ma[2].replace('"','') # erase " on end of crumb
    # ref:
    # https://stackoverflow.com/questions/44030983/yahoo-finance-url-not-working
    # "CrumbStore":\{"crumb":"(?<crumb>[^"]+)"\}
    # SOF syntax does not work for me but it pointed me in the right direction.

    nowutime_s = datetime.datetime.now().strftime("%s")
    csvurl_s   = 'https://query1.finance.yahoo.com/v7/finance/download/'+tkr+'?period1=-631123200&period2='+nowutime_s+'&interval=1d&events=history&crumb='+crumb_s
    csv_r      = ssn.get(csvurl_s)
    csv_s      = csv_r.content.decode("utf-8")
    csv_status_i = csv_r.status_code
    # I should write the csv_s to csv file:
    with open(outdirc+tkr+'.csv','w') as fh:
        fh.write(csv_s)
'bye'

