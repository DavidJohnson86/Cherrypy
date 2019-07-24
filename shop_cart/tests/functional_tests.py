from selenium import webdriver
from time import sleep
import unittest
import HtmlTestRunner
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

# https://www.softwaretestinghelp.com/web-application-testing/
# https://stackoverflow.com/questions/34604344/python-unit-testing-to-test-over-the-loop-and-not-to-break


class LinkTests(unittest.TestCase):
    """Default Test case setup for unit test"""

    DEFAULT_DELAY_TIME = 3

    def setUp(self):
        self.driver = webdriver.Chrome(r'd:\07_Development\Projects\Cherrypy\shop_cart\tests\chromedriver.exe')
        self.driver.get("http:\\127.0.0.1:8080")
        self.driver.implicitly_wait(4)

    def is_element_present(self, how, what):
        """
        Helper method to confirm the presence of an element on page
        :params how: By locator type
        :params what: locator value
        """
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    def tearDown(self) -> None:
        self.driver.close()


# def test_gen_link(link):
#     def test_method(self):
#         elem = self.driver.find_element_by_link_text(link)
#         elem.click()
#         sleep(LinkTests.DEFAULT_DELAY_TIME)
#         return self.assertTrue(self.is_element_present(By.LINK_TEXT, link))
#     return test_method


def test_gen_link(link):
    def test_method(self):
        elem = self.driver.find_element_by_link_text(link)
        elem.click()
        sleep(LinkTests.DEFAULT_DELAY_TIME)
        return self.assertTrue(self.is_element_present(By.LINK_TEXT, link))
    return test_method

class LinkTestSpecification:
    """" Test the outgoing links from all the pages to the specific domain under test.
         Test all internal links.
         Test links jumping on the same pages.
         Test links used to send email to admin or other users from web pages.
         Test to check if there are any orphan pages.
         Finally, link checking includes, check for broken links in all above-mentioned links."""

    def __init__(self):
        self.driver = webdriver.Chrome(r'd:\07_Development\Projects\Cherrypy\shop_cart\tests\chromedriver.exe')
        self.driver.get("http:\\127.0.0.1:8080")
        self.driver.implicitly_wait(3)

    def text_link_tests(self):
        """Define tests"""

        links = self.driver.find_elements_by_xpath("//a[@href]")
        for link in links:
            link = link.get_attribute("text")
            test_name = 'test_link_{0}'.format(link)  # define method name
            test = test_gen_link(link)  # define method and its contents
            setattr(LinkTests, test_name, test)

    # def picture_link_tests(self):
    #     driver = webdriver.Chrome(r'd:\07_Development\Projects\Cherrypy\shop_cart\tests\chromedriver.exe')
    #     driver.get("http:\\127.0.0.1:8080")
    #     images = driver.find_elements_by_tag_name('img')
    #     for image in images:
    #         image = image.get_attribute()
    #         test_name = 'test_link_{0}'.format(image)  # define method name
    #         test = test_gen_link(image)  # define method and its contents
    #         setattr(LinkTests, test_name, test)



if __name__ == '__main__':
    LinkTestSpecification().text_link_tests()
   # LinkTestSpecification().picture_link_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(LinkTests)
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'./reports'))