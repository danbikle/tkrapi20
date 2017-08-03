"""
flaskr.py

Demo:
export FLASK_DEBUG=1
export PORT=5011
python flaskr.py
Other shell:
curl localhost:5011/demo11.json
curl localhost:5011/static/hello.json
"""

import os
import flask
import flask_restful as fr

application = flask.Flask(__name__)
api         = fr.Api(application)

class Demo11(fr.Resource):
  def get(self):
    my_k_s = 'hello'
    my_v_s = 'world'
    return {my_k_s: my_v_s}
api.add_resource(Demo11, '/demo11.json')

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  application.run(host='0.0.0.0', port=port)
'bye'
