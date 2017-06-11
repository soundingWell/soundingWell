#!/usr/bin/python

### GAE ###
from google.appengine.ext import ndb
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

### Basics ###
import json
import sys

# What does this do?
sys.path.append('python/')

class MainPage(webapp.RequestHandler):
    
    def get(self):
        # print 'yuppo'
        path = 'html/main.html'
        template_values = {}
        self.response.out.write(template.render(path, template_values))    
    
application = webapp.WSGIApplication([('/', MainPage)],
                                       debug=True)

def main():
    run_wsgi_app(application)


if __name__ == "__main__":
    main()