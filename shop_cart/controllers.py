"""Login Page Example"""
# pylint --disable=F0401 cherrypy
import config
import cherrypy
from jinja2 import Environment, FileSystemLoader

class WebService:
    """This class should be inherited for different pages"""

    TEMPLATE_FOLDER = r"./views"

    def __init__(self, html_template_file_name):
        """Initialize variables"""
        self._environment = Environment(loader=FileSystemLoader(WebService.TEMPLATE_FOLDER))
        self._html_file = self._environment.get_template(html_template_file_name)


class HomePage(WebService):


    datas = {"ring": {"path": "product-details/ring",
                      "img:": "assets/img/bootstrap-ring.png",
                      "price": "140",
                      "desc":  "Nowadays the lingerie industry is one of the most successful business spheres."
                               "We always stay in touch with the latest fashion tendencies - that is why our goods are "
                               "so popular.."},
             "purple_necklace": {"path": "product-details/purple_necklace",
                                 "img:": "assets/img/bootstrap-ring.png",
                                 "price": "140",
                                 "desc": "Nowadays the lingerie industry is one of the most successful business spheres."
                                         "We always stay in touch with the latest fashion tendencies - that is why "
                                         "our goods are so popular.."}
                        }

    new_products = {"product-details/ring": "assets/img/bootstrap-ring.png",
                    "product-details/purple_necklace": "assets/img/i.jpg",
                    "product-details/golden_ring": "assets/img/g.jpg",
                    "product-details/colorful_necklace": "assets/img/s.png",
                    "product-details/purple_heart_necklace": "assets/img/i.jpg",
                    "product-details/queen_necklace": "assets/img/f.jpg",
                    "product-details/golden_ring2": "assets/img/h.jpg",
                    "product-details/blue_silver_ring": "assets/img/j.jpg",
                    }

    products = {"product-details/queen_golden_bracelet": "assets/img/b.jpg",
                "product-details/rings": "assets/img/c.jpg",
                "product-details/golden_watch": "assets/img/a.jpg"}

    featured_products = {"product-details/silver_rings": "assets/img/d.jpg",
                         "product-details/golden_ring": "assets/img/e.jpg",
                         "product-details/queen_necklace": "assets/img/f.jpg"}

    @cherrypy.expose
    def index(self):
        return self._html_file.render(new_products=HomePage.new_products,
                                      products=HomePage.new_products,
                                      featured_products= HomePage.featured_products)


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


class ProductsPage(WebService):

    @cherrypy.expose
    def index(self):
        return self._html_file.render()

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
    WEBAPP.cart = CartPage('cart.html')
    WEBAPP.compair = ComPairPage()
    WEBAPP.contact = ContactPage('contact.html')
    WEBAPP.list_view = ListViewPage('list-view.html')
    WEBAPP.grid_view = GridViewPage('grid-view.html')
    WEBAPP.forget_password = ForgetPasswordPage()
    WEBAPP.general = GeneralPage('general.html')
    WEBAPP.header = HeaderPage()
    WEBAPP.login = LoginPage()
    WEBAPP.product_details = ProductDetailsPage()
    WEBAPP.products = ProductsPage('products.html')
    WEBAPP.register = RegisterPage('register.html')
    cherrypy.quickstart(WEBAPP, '/', config.cherrpy_run_conf)
