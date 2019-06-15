"""Login Page Example"""
# pylint --disable=F0401 cherrypy
import re
from time import time
import config
import cherrypy
import models.database_handler as db
from jinja2 import Environment, FileSystemLoader

# TODO css input field for html templates

class WebService:
    """This class should be inherited for different pages"""

    TEMPLATE_FOLDER = r"./views"

    def __init__(self, html_template_file_name):
        """Initialize variables"""
        self._environment = Environment(loader=FileSystemLoader(WebService.TEMPLATE_FOLDER))
        self._html_file = self._environment.get_template(html_template_file_name)


class StorePage(WebService):
    """If user authorized returns welcome screen"""

    def _cp_dispatch(self, vpath):
        """Perform URI dispatching for store services"""

        if len(vpath) == 0:
            return self

        if len(vpath) == 1:
            cherrypy.request.params['product'] = vpath.pop(0)
            return ProductPage('product.html')


    @cherrypy.expose
    def index(self):
        """User must to be authorized to access this page"""
        if cherrypy.session['authorized'] is True:
            products_table = db.MySqlHandler('products')
            columns = [col for col in products_table.get_column_name(products_table.tables)]
            items = [item for item in products_table.set_store_details()]
            return self._html_file.render(columns=columns, items=items)
        return 'error.html'


class ProductPage(WebService):


    @cherrypy.expose
    def index(self, product):
        cherrypy.log(product)
        return self._html_file.render(Title=product,
                                      Hint='Please enter credentials to login.',
                                      Href_Text='Register',
                                      Href_Link='/register',
                                      Guide='Don not have an account ? Please',
                                      ActionBtn='Login')


# pylint: disable=C0103
class LoginWebService(WebService):
    """Serves as login web service which is responsible for user login etc..."""

    @cherrypy.expose
    def index(self):
        """Refers to LoginPage"""
        return self._html_file.render(Title='Login',
                                      Hint='Please enter credentials to login.',
                                      Href_Text='Register',
                                      Href_Link='/register',
                                      Guide='Don not have an account ? Please',
                                      ActionBtn='Login')

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        """GET method implementation"""
        cherrypy.session['ts'] = time()
        cherrypy.log(cherrypy.session['ts'])

    @cherrypy.expose
    def POST(self, **kwargs):
        """
        POST method for REST user credentials handling.

        Args:
            **kwargs: {user: pw}

        Returns:
            string to the JS

        """
        name = kwargs['name']
        pw = kwargs['pw']
        validate = db.SqLiteHandler().sql_query("user_credentials", name, "name,pw")
        if validate and name != validate[0][0]:
            return "INV_USER"
        else:
            if validate[0][1] == pw:
                cherrypy.session['authorized'] = True
                return "VERIFIED"
        return "WRONG PASSWORD"

    def PUT(self, string):
        """
        Update resource
        Args:
            string(str): Could be a state or anyting else

        Returns:

        """
        cherrypy.session['authorized'] = string

    def DELETE(self):
        """DELETE HTTP METHOD"""
        cherrypy.session.pop('authorized', None)

    def validate_mail(self, email):
        """Validate email"""
        match = re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]*\.*[com|org|edu]{3}$)", email)
        return bool(match)


class RegisterWebService(WebService):
    """Page for register"""

    @cherrypy.expose
    def index(self):
        """Refers to register page"""
        return self._html_file.render(Title='Register',
                                      Hint='Please fill in this form to create an account.',
                                      Guide='Already have an account ?',
                                      Href_Text='Login',
                                      Href_Link='/',
                                      ActionBtn='Register')

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        """GET implementation"""
        cherrypy.session['ts'] = time()
        cherrypy.log(cherrypy.session['ts'])


if __name__ == '__main__':
    cherrypy.config.update({'log.screen': True,
                            'log.access_file': '',
                            'log.error_file': 'error.txt'})
    WEBAPP = LoginWebService('login.html')
    WEBAPP.store = StorePage('store.html')
    WEBAPP.login = LoginWebService('login.html')
    WEBAPP.register = RegisterWebService('login.html')
    cherrypy.quickstart(WEBAPP, '/', config.cherrpy_run_conf)
