from flask import Flask, make_response, session, redirect, url_for, escape, request
app = Flask(__name__)

from app import modules
modules.get()
from app import routes
routes.static()