from app import app
import os
from flask_sqlalchemy import SQLAlchemy, create_engine
dialect = os.getenv("DB_DIALECT")
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
database = os.getenv("DB_NAME")
#engine = create_engine('postgresql://scott:tiger@localhost:5432/mydatabase')
