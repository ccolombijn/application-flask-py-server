from app import app
from app import config
import importlib.util
obj = {}

def add(prop,module):
    obj[prop] = module
    
def run(prop):
    return obj[prop].default()
def get():
    modules = config.get()['modules']
    i = 0
    while(i < len(modules)):
        spec = importlib.util.spec_from_file_location('default', '''modules/''' + modules[i] + '''.py''')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        add(modules[i],module)
        print(module)
        i+=1