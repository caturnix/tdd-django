from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from django.test import LiveServerTestCase
import time
from selenium.webdriver.common.keys import Keys

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):
	def setUp(self):
		# setting up route to firefox executable as it wasnt installed systemwide
		self.binary = FirefoxBinary('/Users/vvperepelkin/desktop/Firefox.app/Contents/MacOS/firefox')
		self.browser = webdriver.Firefox(firefox_binary=self.binary)

	def tearDown(self):
		self.browser.quit()

	def wait_for_row_in_list_table(self, row_text):
		start_time=time.time()
		while True:
			try:
				table=self.browser.find_element_by_id('id_list_table')
				rows=table.find_elements_by_tag_name('tr')
				self.assertIn(row_text, [row.text for row in rows])
				return
			except (AssertionError, WebDriverException) as e:
				if time.time() - start_time > MAX_WAIT:
					raise e
				time.sleep(0.5)

	def test_can_start_a_list_and_retieve_it_later(self):
		# opening homepage
		self.browser.get(self.live_server_url)

		# user notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text=self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# user is invited to enter a to-do list straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		# user enters "Buy feathers" into a text box
		inputbox.send_keys('Buy feathers')

		# user hits enter, the page updates, and the page lists "1: Buy feathers" as an item to-do list
		inputbox.send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Buy feathers')

# there is still textbox inviting to add another item
# user enters "Use feathers to make a fly"
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)
		inputbox.send_keys('Use feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
# the page updates again and shows both items in a list

		self.wait_for_row_in_list_table('1: Buy feathers')
		self.wait_for_row_in_list_table('2: Use feathers to make a fly')

# user sees that the site has generated a unique URL for him
# there is explanatory text for this effect

# User visits this unique URL and the to-do list is still there

# User leaves the site
		self.fail('Finish the test!')
