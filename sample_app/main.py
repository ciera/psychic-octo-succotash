# run: dev_appserver.py app.yaml

import webapp2
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self): #for a get request
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!') #the response

class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_env.get_template('templates/welcome.html')
        self.response.write(welcome_template.render())

app = webapp2.WSGIApplication([
    ('/', MainPage), #this maps the root url to the Main Page Handler
    ('/enterinfo', EnterInfoHandler)
], debug=True)
