import os.path
import cherrypy

conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())},

        '/logined': {
                'tools.sessions.on': True,
                'tools.staticdir.root': os.path.abspath(os.getcwd())},

        '/generator': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/public': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }


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
        self._database = {'name': 'admin', 'pw': 'admin'}

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return cherrypy.session['mystring']

    def POST(self, **kwargs):
        name = kwargs['name']
        pw = kwargs['pw']
        if name not in self._database.values():
            return "INV_USER"
        else:
            if self._database['pw'] == pw:
                cherrypy.session['authorized'] = True
                return "VERIFIED"
            else:
                return "WRONG PASSWORD"

    def PUT(self, another_string):
        cherrypy.session['mystring'] = another_string

    def DELETE(self):
        cherrypy.session.pop('mystring', None)


if __name__ == '__main__':
    webapp = LoginPage()
    webapp.logined = VerifiedPage()
    webapp.generator = LoginWebService()
    cherrypy.quickstart(webapp, '/', conf)