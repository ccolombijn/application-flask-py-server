from flask import Flask, make_response, session, redirect, url_for, send_from_directory, escape, request, render_template
app = Flask(__name__, static_url_path='/assets')
app.config['EXPLAIN_TEMPLATE_LOADING'] = True
from app import modules
modules.get()
from app import routes
routes.static()