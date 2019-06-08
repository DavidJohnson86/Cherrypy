"""Login Page Example"""
import cherrypy
import config
import re
from time import time
import models.database_handler as db
from jinja2 import Environment, FileSystemLoader


class WebService:
    """This class should be inherited for different pages"""

    TEMPLATE_FOLDER = r"./views"

    def __init__(self, html_template_file_name):
        """Initialize variables"""
        self._environment = Environment(loader=FileSystemLoader(WebService.TEMPLATE_FOLDER))
        self._html_file = self._environment.get_template(html_template_file_name)


class VerifiedPage(WebService):
    """If user authorized returns welcome screen"""
    @cherrypy.expose
    def index(self):
        if cherrypy.session['authorized'] is True:
            prods = db.MySqlHandler()
            prods.select_query('products')
            column_content = '  '.join([i for i in prods.get_column_name('')])
            body_content = ""
            for elem in prods.select_query('products'):
                cherrypy.log(str(elem))
                body_content += "<p>"
                for j in elem:
                    cherrypy.log(str(j))
                    body_content += "****{0}>****".format(j)
                """ body_content = [y for prod in prods.select_query('products') for y in prod]"""
                body_content+="</p>"
            return self._html_file.render(COLUMNS=column_content,
                                          CONTENT=body_content)
        else:
            return 'error.html'


class LoginWebService(WebService):
    """Serves as login web service which is responsible for user login etc..."""

    @cherrypy.expose
    def index(self):
        return self._html_file.render(Title='Login',
                                      Hint='Please enter credentials to login.',
                                      Href_Text='Register',
                                      Href_Link='/register',
                                      Guide='Don not have an account ? Please',
                                      ActionBtn='Login')

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        cherrypy.session['ts'] = time()
        cherrypy.log(cherrypy.session['ts'])

    @cherrypy.expose
    def POST(self, **kwargs):
        name = kwargs['name']
        pw = kwargs['pw']
        validate = db.SqLiteHandler().sql_query("user_credentials", name, "name,pw")
        if validate and name != validate[0][0]:
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

    def validate_mail(self, email):
        match = re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]*\.*[com|org|edu]{3}$)", email)
        if match:
            return True
        else:
            return False


class RegisterWebService(WebService):
    """Page for register"""

    @cherrypy.expose
    def index(self):
        return self._html_file.render(Title='Register',
                                      Hint='Please fill in this form to create an account.',
                                      Guide='Already have an account ?',
                                      Href_Text='Login',
                                      Href_Link='/',
                                      ActionBtn='Register')

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        cherrypy.session['ts'] = time()
        cherrypy.log(cherrypy.session['ts'])


if __name__ == '__main__':
    cherrypy.config.update({'log.screen': True,
                            'log.access_file': '',
                            'log.error_file': 'error.txt'})
    webapp = LoginWebService('login.html')
    webapp.verified = VerifiedPage('logined.html')
    webapp.register = RegisterWebService('login.html')
    cherrypy.quickstart(webapp, '/', config.cherrpy_run_conf)
