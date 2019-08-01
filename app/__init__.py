from flask import Flask, make_response, session, redirect, url_for, escape, request, render_template
app = Flask(__name__)
app.config['EXPLAIN_TEMPLATE_LOADING'] = True
from app import modules
modules.get()
from app import routes
routes.static()