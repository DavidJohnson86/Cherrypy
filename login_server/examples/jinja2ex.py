import cherrypy
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('views'))

class Root:
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('login.html')
        return tmpl.render(salutation='Hello', target='World')

cherrypy.config.update({'server.socket_host': '127.0.0.1',
                         'server.socket_port': 8080,
                        })

cherrypy.quickstart(Root())