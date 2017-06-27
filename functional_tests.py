from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		# setting up route to firefox executable as it wasnt installed systemwide
		self.binary = FirefoxBinary('/Users/vvperepelkin/desktop/Firefox.app/Contents/MacOS/firefox')
		self.browser = webdriver.Firefox(firefox_binary=self.binary)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retieve_it_later(self):
		# opening homepage
		self.browser.get('http://localhost:8000')

		# user notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')


# Functional tests



# user is invited to enter a to-do list straight away

# user enters "Buy feathers" into a text box

# user hits enter, the page updates, and the page lists "1: Buy feathers" as an item to-do list

# there is still textbox inviting to add another item

# user enters "Use feathers to make a fly"

# the page updates again and shows both items in a list

# user sees that the site has generated a unique URL for him
# there is explanatory text for this effect

# User visits this unique URL and the to-do list is still there

# User leaves the site

if __name__ == '__main__':
	unittest.main(warnings='ignore')