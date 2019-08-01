from app import app
from app import config
def get(obj):
    config = config.get()
    if obj['template']:
        template = obj['template']
    else:
        template = config.defaults['template']
    
    name = obj['name']
    return render_template('''templates/''' + template + '''.html''', name = name)