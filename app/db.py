from app import app, settings
import mysql.connector
import json
import os
connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        passwd=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
def conn():
    return connection
    
def query(sql):
    return conn().cursor().execute(sql)

def request(req):
    req.setdefault('method','get')
    if req.method == 'get':
        method = 'SELECT'
    #cols = ','.join(tup)
    sql = method +' ' + req.table
    return query(sql)
    
def response(res):
    #res = db.query(sql)
    #res = db.response(res.fetchall())
    #json = json.dumps(res)
    row_headers=[x[0] for x in res.description]
    data=[]
    for result in res:
        data.append(dict(zip(row_headers,result)))
    return data

