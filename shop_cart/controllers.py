"""Login Page Example"""
# pylint --disable=F0401 cherrypy
import config
import cherrypy
import os


class HomePage:
    @cherrypy.expose
    def index(self):
        return open(r'views\index.html')


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

class FourColPage:

    @cherrypy.expose
    def index(self):
        return open(r'views\four-col.html')

class GeneralPage:

    @cherrypy.expose
    def index(self):
        return open(r'views\general.html')


class HeaderPage:

    @cherrypy.expose
    def index(self):
        return open(r'views\header.html')


class GridPage:

    @cherrypy.expose
    def index(self):
        return open(r'views\grid-view.html')


class ListViewPage:

    @cherrypy.expose
    def index(self):
        return open(r'views\list-view.html')


class LoginPage:

    @cherrypy.expose
    def index(self):
        return open(r'views\login.html')


class ProductsPage:

    @cherrypy.expose
    def index(self):
        return open(r'views\products.html')


class ProductDetailsPage:

    @cherrypy.expose
    def index(self):
        return open(r'views\product-details.html')


class RegisterPage:

    @cherrypy.expose
    def index(self):
        return open(r'views\register.html')


class ThreeColPage:

    @cherrypy.expose
    def index(self):
        return open(r'views\three-col.html')



if __name__ == '__main__':
    cherrypy.config.update({'log.screen': True,
                            'log.access_file': '',
                            'log.error_file': 'error.txt'})
    WEBAPP = HomePage()
    WEBAPP.cart = CartPage()
    WEBAPP.compair = ComPairPage()
    WEBAPP.contact = ContactPage()
    WEBAPP.forget_password = ForgetPasswordPage()
    four_col = "four-col"
    grid_view ="grid-view"
    WEBAPP.four_col = FourColPage()
    WEBAPP.general = GeneralPage()
    WEBAPP.grid_view = GridPage()
    WEBAPP.header = HeaderPage()
    list_view = "list-view"
    WEBAPP.list_view = ListViewPage()
    WEBAPP.login = LoginPage()
    product_details = "product-details"
    WEBAPP.product_details = ProductDetailsPage()
    WEBAPP.products = ProductsPage()
    WEBAPP.register = RegisterPage()
    three_col = "three-col"
    WEBAPP.three_col = ThreeColPage()
    cherrypy.quickstart(WEBAPP, '/', config.cherrpy_run_conf)
