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


class ContactPage(WebService):
    #todo layout of the google map should be optimized
    @cherrypy.expose
    def index(self):
        return self._html_file.render()


class ForgetPasswordPage:

    @cherrypy.expose
    def index(self):
        return open(r'views\forget_password.html')

class GridViewPage(WebService):

    @cherrypy.expose
    def index(self):
        return self._html_file.render()


class GeneralPage(WebService):

    @cherrypy.expose
    def index(self):
        return self._html_file.render()


class ListViewPage(WebService):

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

class ThreeColPage(WebService):

    @cherrypy.expose
    def index(self):
        return self._html_file.render()


@cherrypy.popargs('product')
class ProductDetailsPage:
    @cherrypy.expose
    def index(self, product):
        return open(r'views\product-details.html')


class RegisterPage(WebService):

    @cherrypy.expose
    def index(self):
        return self._html_file.render()


if __name__ == '__main__':
    cherrypy.config.update({'log.screen': True,
                            'log.access_file': '',
                            'log.error_file': 'error.txt'})
    product_details = "product-details"
    list_view = "list-view"
    grid_view = "grid-view"
    WEBAPP = HomePage('index.html')
    WEBAPP.cart = CartPage()
    WEBAPP.compair = ComPairPage()
    WEBAPP.contact = ContactPage('contact.html')
    WEBAPP.list_view = ListViewPage('list-view.html')
    WEBAPP.grid_view = GridViewPage('grid-view.html')
    WEBAPP.forget_password = ForgetPasswordPage()
    WEBAPP.general = GeneralPage('general.html')
    WEBAPP.header = HeaderPage()
    WEBAPP.login = LoginPage()
    WEBAPP.product_details = ProductDetailsPage()
    WEBAPP.products = ProductsPage()
    WEBAPP.register = RegisterPage('register.html')
    cherrypy.quickstart(WEBAPP, '/', config.cherrpy_run_conf)
