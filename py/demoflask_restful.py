"""
demoflask_restful.py

This script should demo flaskRESTful.

https://flask-restful.readthedocs.io
https://github.com/flask-restful/flask-restful

Demo:
Shell 1:
export PORT=5050
export FLASK_DEBUG=1
~/anaconda3/bin/python demoflask_restful.py
The above shell will then be busy as a server.
So, leave it alone.


Shell 2:
Shell 2 should send calls to the server in Shell 1.

I should try this shell command in Shell 2:
curl                            localhost:5050/hello.json
curl -d 'msg2flask=hello-flask' localhost:5050/hello.json
"""

import flask         as fl
import flask_restful as fr
import pdb
import os

# I should ready flask_restful:
application = fl.Flask(__name__)
api         = fr.Api(application)
  
class Hello(fr.Resource):
  """
  This class should be a simple syntax demo.
  """
  def get(self):
    my_k_s = 'hello'
    my_v_s = 'world'
    return {my_k_s: my_v_s}

  def post(self):
    my_k_s    = 'post-hello'
    my_v_s    = 'world'
    curlmsg_s = fl.request.form['msg2flask']
    return {my_k_s: my_v_s, 'curlmsg': curlmsg_s}

api.add_resource(Hello, '/hello.json')
  
if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5050))
  application.run(host='0.0.0.0', port=port)
'bye'


