"""
request_tkr.py

This script should get price data.
"""

import requests
import pdb

pdb.set_trace()

tkr = '^GSPC'
user_agent_s = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'

tkr_r = requests.get('https://www.python.org')
print(tkr_r.status_code)

html_s = tkr_r.content
print(html_s[:55])

'bye'

