from app import app
name = 'Dashboard'
def default():
    print('This is dashboard')
    return {'name': name }