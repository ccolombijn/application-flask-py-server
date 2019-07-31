from app import app
from app import config
from flask import Flask, session, redirect, url_for, escape, request,make_response
import json

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