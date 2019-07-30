# pylint --disable=F0401 cherrypy
import config
import cherrypy
from models.data import products
from jinja2 import Environment, FileSystemLoader

class WebService:
    """This class should be inherited for different pages"""

    TEMPLATE_FOLDER = r"./views"

    def __init__(self, html_template_file_name):
        """Initialize variables"""
        self._environment = Environment(loader=FileSystemLoader(WebService.TEMPLATE_FOLDER))
        self._html_file = self._environment.get_template(html_template_file_name)


class HomePage(WebService):
    """As a webstore homepage welcomes with the product selection."""

    featured_products = [i for i in products if i["type"] == "featured"]
    new_products = [i for i in products if i["type"] == "new"]
    products = [i for i in products if i["type"] == "normal"]

    @cherrypy.expose
    def index(self):
        return self._html_file.render(new_products=HomePage.new_products,
                                      products=HomePage.products,
                                      featured_products=HomePage.featured_products)


class CartPage(WebService):

    @cherrypy.expose
    def index(self):
        return self._html_file.render()


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

    products = [i for i in products][0]

    @cherrypy.expose
    def index(self):
        return self._html_file.render(products=products)


class HeaderPage:

    @cherrypy.expose
    def index(self):
        return open(r'views\header.html')


class LoginPage:

    @cherrypy.expose
    def index(self):
        return open(r'views\login.html')


class ProductsPage(WebService):

    @cherrypy.expose
    def index(self):
        return self._html_file.render()

class ThreeColPage(WebService):

    @cherrypy.expose
    def index(self):
        return self._html_file.render()


@cherrypy.popargs('product')
class ProductDetailsPage(WebService):

    @cherrypy.expose
    def index(self, product):
        choosen_product = [i for i in products if i['path'].split('/')[-1] == product ][0]
        return self._html_file.render(product=choosen_product)


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
    WEBAPP.cart = CartPage('cart.html')
    WEBAPP.compair = ComPairPage()
    WEBAPP.contact = ContactPage('contact.html')
    WEBAPP.list_view = ListViewPage('list-view.html')
    WEBAPP.grid_view = GridViewPage('grid-view.html')
    WEBAPP.forget_password = ForgetPasswordPage()
    WEBAPP.general = GeneralPage('general.html')
    WEBAPP.header = HeaderPage()
    WEBAPP.login = LoginPage()
    WEBAPP.product_details = ProductDetailsPage('product-details.html')
    WEBAPP.products = ProductsPage('products.html')
    WEBAPP.register = RegisterPage('register.html')
    cherrypy.quickstart(WEBAPP, '/', config.cherrpy_run_conf)
