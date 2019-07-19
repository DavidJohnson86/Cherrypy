"""Login Page Example"""
# pylint --disable=F0401 cherrypy
import config
import cherrypy
from jinja2 import Environment, FileSystemLoader
import os



class WebService:
    """This class should be inherited for different pages"""

    TEMPLATE_FOLDER = r"./views"

    def __init__(self, html_template_file_name):
        """Initialize variables"""
        self._environment = Environment(loader=FileSystemLoader(WebService.TEMPLATE_FOLDER))
        self._html_file = self._environment.get_template(html_template_file_name)

class HomePage(WebService):
    @cherrypy.expose
    def index(self):
        return self._html_file.render()


class CartPage:

    @cherrypy.expose
    def index(self):
        return open(r'views\cart.html')


class ComPairPage:

    @cherrypy.expose
    def index(self):
        return open(r'views\compair.html')

class ContactPage:

    @cherrypy.expose
    def index(self):
        return open(r'views\contact.html')


class ForgetPasswordPage:

    @cherrypy.expose
    def index(self):
        return open(r'views\forget_password.html')


class GeneralPage(WebService):

    @cherrypy.expose
    def index(self):
        return self._html_file.render()


class HeaderPage:

    @cherrypy.expose
    def index(self):
        return open(r'views\header.html')


class LoginPage:

    @cherrypy.expose
    def index(self):
        return open(r'views\login.html')


class ProductsPage:

    @cherrypy.expose
    def index(self):
        return open(r'views\products.html')


@cherrypy.popargs('product')
class ProductDetailsPage:
    @cherrypy.expose
    def index(self, product):
        return open(r'views\product-details.html')


class RegisterPage:

    @cherrypy.expose
    def index(self):
        return open(r'views\register.html')


if __name__ == '__main__':
    cherrypy.config.update({'log.screen': True,
                            'log.access_file': '',
                            'log.error_file': 'error.txt'})
    WEBAPP = HomePage('index.html')
    WEBAPP.cart = CartPage()
    WEBAPP.compair = ComPairPage()
    WEBAPP.contact = ContactPage()
    WEBAPP.forget_password = ForgetPasswordPage()
    WEBAPP.general = GeneralPage('general.html')
    WEBAPP.header = HeaderPage()
    WEBAPP.login = LoginPage()
    product_details = "product-details"
    WEBAPP.product_details = ProductDetailsPage()
    WEBAPP.products = ProductsPage()
    WEBAPP.register = RegisterPage()
    cherrypy.quickstart(WEBAPP, '/', config.cherrpy_run_conf)
