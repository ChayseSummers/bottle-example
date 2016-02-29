import bottle
import random

APP = bottle.default_app()

@APP.route('/')
def index():
  return '<p>Hello</p>'
  
@APP.route('/myRandom')
def myRandom():
  return '<p>Random page!</p>'

if __name__ == '__main__':
  bottle.run(application=APP)
