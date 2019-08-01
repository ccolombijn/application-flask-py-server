from app import app, request, send_from_directory, make_response
from app import config
from app import modules
from app import template

import json
def static():
    @app.route('/<path:path>')
    def send(path):
        return send_from_directory('assets', path)
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
    print('''Added route ''' + attr)
    @app.route(attr)
    def some():
        res = modules.run(value)
        return template.get(res)
        
