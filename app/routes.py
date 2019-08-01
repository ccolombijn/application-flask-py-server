from app import app
from app import config
from app import modules
from flask import Flask, session, redirect, url_for, escape, request,make_response
import json
def static():
    @app.route('/')
    @app.route('/index')
    def index():
        return '''
        <html>
        <head>
            <title>''' + config.get()['name'] + '''</title>
        </head>
        <body>
            <h1>''' + config.get()['name'] + '''</h1>
        </body>
        </html>'''
    @app.route('/config')
    def config_():
        res = make_response(json.dumps(config.get()))
        res.mimetype = 'application/json'
        return res

for attr, value in config.get()['routes'].items():
    print('''Added route /''' + attr)
    @app.route('''/''' + attr)
    def some():
        res = modules.run(value)
        return res
        
