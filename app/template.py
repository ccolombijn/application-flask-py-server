from app import app
from app import config
def get(obj):
    name = obj['name']
    return '''
        <html>
        <head>
            <title>''' + name + '''</title>
        </head>
        <body>
            <h1>''' + name + '''</h1>
        </body>
        </html>'''