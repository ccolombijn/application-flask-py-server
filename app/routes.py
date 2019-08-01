from app import app
from app import config
from app import modules
from app import template
from flask import Flask, session, redirect, url_for, escape, request,make_response
import json
def static():
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
        
