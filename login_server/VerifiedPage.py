"""Login Page Example"""
import cherrypy
import os.path
import requests
from cherrypy import dispatch
from time import time
import database.database_handler as db


class LoginPage:
    """This is the login page which returns authentication html"""
    @cherrypy.expose
    def index(self):
        return open('index.html')


class VerifiedPage:
    """If user authorized returns welcome screen"""
    @cherrypy.expose
    def index(self):
        if cherrypy.session['authorized'] is True:
            return open('logined.html')
        else:
            return 'error.html'


@cherrypy.expose
class LoginWebService(object):

    def __init__(self):
        pass
    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        cherrypy.session['ts'] = time()
        cherrypy.log(cherrypy.session['ts'])

    def POST(self, **kwargs):
        name = kwargs['name']
        pw = kwargs['pw']
        validate = db.SqLiteHandler().sql_query("user_credentials", name, "name,pw")
        if name != validate[0][0]:
            return "INV_USER"
        else:
            if validate[0][1] == pw:
                cherrypy.session['authorized'] = True
                return "VERIFIED"
            else:
                return "WRONG PASSWORD"

    def PUT(self, another_string):
        cherrypy.session['authorized'] = another_string

    def DELETE(self):
        cherrypy.session.pop('authorized', None)


cherrpy_run_conf = {

        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd()),
            'tools.proxy.on': True,
            'tools.response_headers.on': True,
            },

        '/logined': {
                'tools.sessions.on': True,
                'tools.staticdir.root': os.path.abspath(os.getcwd())},

        '/generator': {
            'request.dispatch': dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/public': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public',

        }
    }

if __name__ == '__main__':
    webapp = LoginPage()
    webapp.logined = VerifiedPage()
    webapp.generator = LoginWebService()
    cherrypy.quickstart(webapp, '/', cherrpy_run_conf)
