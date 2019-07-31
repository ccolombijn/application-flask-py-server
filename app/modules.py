from app import app
from app import config
import importlib.util
def get():
    modules = config.get()['modules']
    i = 0
    while(i < len(modules)):
        spec = importlib.util.spec_from_file_location('default', '''modules/''' + modules[i] + '''.py''')
        module = importlib.util.module_from_spec(spec)
        print(module)
        spec.loader.exec_module(module)
        module.default()
        i+=1
        