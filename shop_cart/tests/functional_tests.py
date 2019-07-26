from selenium import webdriver
from time import sleep
import unittest
import HtmlTestRunner
import requests

# https://www.softwaretestinghelp.com/web-application-testing/
# https://stackoverflow.com/questions/34604344/python-unit-testing-to-test-over-the-loop-and-not-to-break


class LinkTests(unittest.TestCase):
    """Default Test case setup for unit test"""

    DEFAULT_DELAY_TIME = 0.15

    @classmethod
    def test_gen_link(cls, link):
        def test_method(self):
            r = requests.get(link)
            sleep(LinkTests.DEFAULT_DELAY_TIME)
            return self.assertTrue(r.ok)
        return test_method


class LinkTestSpecification:
    """" Test the outgoing links from all the pages to the specific domain under test.
         Test all internal links.
         Test links jumping on the same pages.
         Test links used to send email to admin or other users from web pages.
         Test to check if there are any orphan pages.
         Finally, link checking includes, check for broken links in all above-mentioned links."""

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(r'd:\07_Development\Projects\Cherrypy\shop_cart\tests\chromedriver.exe', chrome_options=options)
        self.driver.get("http:\\127.0.0.1:8080")
        self.driver.implicitly_wait(3)

    def text_link_tests(self):
        # todo create link class
        """Define tests"""
        links = list(set(self.driver.find_elements_by_xpath("//a[@href]")))
        for idx, link in enumerate(links):
            link_path = link.get_attribute('href')
            link_name = link.text.replace("\n", "")
            link_path_tail = '/'.join(link_path.split("/")[3:])
            test_name = f'test_case_{idx} LINK: {"NOT DEFINED" if not link_name else link_name} PATH: {link_path_tail}'
            test = LinkTests().test_gen_link(link_path)  # define method and its contents
            setattr(LinkTests, test_name, test)


if __name__ == '__main__':
    LinkTestSpecification().text_link_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(LinkTests)
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'./reports',
                                                           report_title="Link Tests",
                                                           report_name="Functional Tests"))