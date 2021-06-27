from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):    # -> None:
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        # return super().setUp()

    def tearDown(self):     # -> None:
        self.browser.quit()
        # return super().tearDown()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a new cool online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

        # She types "Buy peacock feathers"  into a text box (fly fishing lures)

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an iten in a to-do list

        # There is still a text box inviting her to add anoter item. She
        # enters "Use peacock feathers to make a fly"

        # The page updates again and now shows both items on her list

        # Edith wonders if the site will remember her list. The site
        # generated a unique URL for her

        # She visits that URL - her to-do list is still there

        # Goes back to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')
