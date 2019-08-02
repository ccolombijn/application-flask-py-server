from app import app, request, send_from_directory, make_response
from app import config
from app import modules
from app import template

import json

@app.route('/<path:path>')
def send(path):
    return send_from_directory(config.get()['static'], path)
@app.route('/')
@app.route('/index')
def index():
    return template.get({'name':'Welcome'})
@app.route('/config')
def config_():
    res = make_response(json.dumps(config.get()))
    res.mimetype = 'application/json'
    return res

for attr, value in config.get()['routes'].items():
    print('''\x1b[36m[route]\x1b[1m \x1b[37m''' + attr + '''\x1b[0m\x1b[36m : modules'''+ attr+'''.py\x1b[0m''')
    @app.route(attr)
    def some():
        res = modules.run(value)
        return template.get(res)
        
