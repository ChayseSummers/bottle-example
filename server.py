import bottle
import random

APP = bottle.default_app()

@APP.route('/')
def index():
  return '<p>Hello</p>'
  
@APP.route('/myRandom')
def myRandom():
  return '<p>Random page!</p>'
  
@APP.route('/index')
def index():
  bottle.response.content_type = 'text/html'
  return bottle.static_file('index.html','.')
  
@APP.route('/greet/<salutation>/<name>')
def greet(name):
  return 'Hello %s %s' % (salutaion, name)

if __name__ == '__main__':
  bottle.run(application=APP)
