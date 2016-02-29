import bottle
from random import *

APP = bottle.default_app()

@APP.route('/')
def index():
  return '<p>Hello</p>'
  
@APP.route('/myRandom')
def myRandom():
  return random.randint(0,100)

if __name__ == '__main__':
  bottle.run(application=APP)
