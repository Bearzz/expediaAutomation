##### Python and Selenium to automatically open expedia.com, enter SLC departure, SEA arrival and dates. Output to console

### Import modules/libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
import os
import time

class expediaUnitTest():
 
 ### Create class and initiate environment variables 
	def __init__(self):
		options = webdriver.ChromeOptions()
		options.add_argument('--ignore-certificate-errors')
		options.add_argument('--ignore-ssl-errors')
		dir_path = os.path.dirname(os.path.realpath(__file__))
		chromedriver = dir_path + "/chromedriver"
		os.environ["webdriver.chrome.driver"] = chromedriver
		self.driver = webdriver.Chrome(chrome_options=options, executable_path= chromedriver)


### Launch Chrome expedia.com. Enters flight origin, destination, and dates. Clicks Submit button.
	def gotoexpedia(self):
		self.driver.get("https://www.expedia.com/")
		ui.WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "tab-flight-tab-hp")))
		self.driver.find_element_by_id("tab-flight-tab-hp").click()
		ui.WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "flight-origin-hp-flight")))
		self.driver.find_element_by_id("flight-origin-hp-flight").send_keys('SLC')
		self.driver.find_element_by_id("flight-destination-hp-flight").send_keys('LAX')
		self.driver.find_element_by_id("flight-departing-hp-flight").send_keys('03/01/2018')
		self.driver.find_element_by_id("flight-returning-hp-flight").clear()
		self.driver.find_element_by_id("flight-returning-hp-flight").send_keys('03/05/2018')
		self.driver.find_element_by_class_name('gcw-submit').click()
		time.sleep(10)

# Loops through flightModuleList. Specifies "//*" to select everything in each module, then prints out class attribute name and prices to console. 		
		parentTab = self.driver.find_element_by_id('flightModuleList')
		for selectAll in parentTab.find_elements_by_xpath("//*"):
			if selectAll.get_attribute("class") == 'dollars price-emphasis':
				print (selectAll.get_attribute("class"))
				print (selectAll.text)
		
# Closes Chrome after time.sleep 	
	def teardown(self):
		time.sleep(10)
		self.driver.close()

if __name__ == "__main__":
	obj = expediaUnitTest()
	obj.gotoexpedia()
	obj.teardown()
	

