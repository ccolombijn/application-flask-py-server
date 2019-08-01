from app import app, render_template
from app import config
def get(obj):
    
    if obj.get('template'):
        template = obj['template']
    else:
        template = config.get()['defaults']['template']
    
    name = obj['name']
    return render_template('''templates/''' + template + '''.html''', name = name)