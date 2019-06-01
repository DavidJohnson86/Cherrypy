import os.path
from cherrypy import dispatch
import VerifiedPage

cherrpy_run_conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())},

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

        '/protected/area': {
            'tools.auth_basic.on': True,
            'tools.auth_basic.realm': 'localhost',
            'tools.auth_basic.checkpassword': VerifiedPage.LoginWebService.PUT,
            'tools.auth_basic.accept_charset': 'UTF-8'}

        }
    }
