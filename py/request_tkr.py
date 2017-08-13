"""
request_tkr.py

This script should get price data.
Ref:
https://stackoverflow.com/questions/21736970/using-requests-module-how-to-handle-set-cookie-in-request-response

Demo:
~/anaconda3/bin/python request_tkr.py IBM
"""

import datetime
import os
import re
import requests
import sys
import time
import pdb

if (len(sys.argv) != 2):
  print('I see a problem. Maybe you forgot a tkr?')
  print('Demo:')
  print('~/anaconda3/bin/python '+sys.argv[0]+' IBM')
  sys.exit(1)
  
# I should get the tkr from the command line
tkr = sys.argv[1]

# I should ensure the output folders exist
homef   = os.environ['HOME'] # Like /home/ann
outdirc = homef+'/tkrcsv/'
outdirh = homef+'/tkrhtml/'

os.system('mkdir -p '+outdirh+' '+outdirc)

csv_type_l = ['div','history','split']
for type_s in csv_type_l:
  os.system('mkdir -p '+outdirc+type_s)

# I should prepare to talk to Yahoo:
user_agent_s = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
url1_s       = 'https://finance.yahoo.com/quote/'+tkr
url2_s       = url1_s+'/history?p='+tkr
headers_d    = {'User-Agent': user_agent_s}
qurl_s       = 'https://query1.finance.yahoo.com/v7/finance/download/'
p1p2_s       = '?period1=-631123200&period2='
ie_s         = '&interval=1d&events='

with requests.Session() as ssn:
    tkr1_r = ssn.get(url1_s, headers=headers_d)
    time.sleep(3)
    tkr2_r = ssn.get(url2_s, headers=headers_d)
    html_s = tkr2_r.content.decode("utf-8")
    # use4debug
    with open(outdirh+tkr+'.html','w') as fh:
        fh.write(html_s)
    # use4debug
    # I should extract the value of crumb from a string like this:
    # lhs_html_s+'"CrumbStore":{"crumb":"z6M4ACgDGXK"}'+rhs_html_s
    # Here is how I do it with sed:
    # crum=`sed -n '/CrumbStore/s/^.*CrumbStore":{"crumb":"//p' /tmp/tkr1.html | sed -n '1s/"}.*//p'`
    # The above sed syntax cuts /tmp/tkr1.html into 3 pieces.
    # The crumb I want is in the middle piece.
    
    # Here is a different approach with Python.
    # I should create a regexp with 2-groups.
    # Typically, a group is the syntax inside parenthesis.
    # I should find crumb_s in the 2nd group.
    pattern_re = r'(CrumbStore":{"crumb":")(.+?")'
    pattern_ma = re.search(pattern_re, html_s) # The crumb I want is in pattern_ma[2].
    crumb_s    = pattern_ma[2].replace('"','') # erase " on end of crumb
    # ref:
    # https://stackoverflow.com/questions/44030983/yahoo-finance-url-not-working
    # "CrumbStore":\{"crumb":"(?<crumb>[^"]+)"\}
    # SOF syntax does not work for me but it pointed me in the right direction.
    csv_type_l = ['history']
    for type_s in csv_type_l:
      nowutime_s = datetime.datetime.now().strftime("%s")
      csvurl_s   = qurl_s+tkr+p1p2_s+nowutime_s+ie_s+type_s+'&crumb='+crumb_s
      # Server needs time to remember the cookie-crumb-pair it just served:
      time.sleep(3)
      csv_r  = ssn.get(csvurl_s, headers=headers_d)
      csv_s  = csv_r.content.decode("utf-8")
      csvf_s = outdirc+type_s+'/'+tkr+'.csv'
      if (csv_r.status_code == 200):
        # I should write the csv_s to csv file:
        with open(csvf_s,'w') as fh:
          fh.write(csv_s)
          print('Wrote:', csvf_s)
      else:
        print('GET request of ',tkr, ' failed. So I am trying again...')
        with requests.Session() as ssn2:
          tkr1_r = ssn2.get(url1_s, headers=headers_d)
          time.sleep(5) # slower this time
          tkr2_r     = ssn2.get(url2_s, headers=headers_d)
          html2_s    = tkr2_r.content.decode("utf-8")
          pattern_ma = re.search(pattern_re, html2_s)
          crumb_s    = pattern_ma[2].replace('"','')
          csvurl_s   = qurl_s+tkr+p1p2_s+nowutime_s+ie_s+type_s+'&crumb='+crumb_s
          time.sleep(5)
          csv2_r = ssn2.get(csvurl_s, headers=headers_d)
          csv2_s = csv_r.content.decode("utf-8")
          if (csv2_r.status_code == 200):
            with open(csvf_s,'w') as fh:
              fh.write(csv2_s)
              print('Wrote:', csvf_s)
          else:
            print('GET request of ',tkr, ' failed. Maybe try later.')

'bye'

