"""
request_tkr.py

This script should get price data.
"""

import requests
import pdb

pdb.set_trace()

tkr          = '^GSPC'
user_agent_s = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
url_s        = 'https://finance.yahoo.com/quote/'+tkr
headers_d    = {'User-Agent': user_agent_s}
tkr_r        = requests.get(url_s, headers=headers_d)
print(tkr_r.status_code)

html_s = tkr_r.content.decode("utf-8")
print(html_s.replace('DOCTYPE','hello')[:155])

'bye'

