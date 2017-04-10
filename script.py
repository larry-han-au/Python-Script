from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class WebInstance:
	def __init__(self, name, psw, isVoucher):
		self.userName = userName
		self.passWord = psw
		self.url = "https://www8.pearsonvue.com/Dispatcher?application=Login&action=actStartApp&v=W2L&clientCode=PEARSONLANGUAGE"

	def startInstance(self):
		self.driver = webdriver.Firefox()
		self.driver.get(self.url)

	def processInstance(self):
		self.login()
		self.goToTimePage()
		self.endInstance()

	def login(self):
		usernameEle = self.driver.find_element_by_name('loginusername')
		usernameEle.send_keys(self.userName)
		passwordEle = self.driver.find_element_by_name('loginpassword')
		passwordEle.send_keys(self.passWord)
		submitEle = self.driver.find_element_by_name('submitlogin')
		submitEle.click()

	def goToTimePage(self):
		time.sleep(5)
		self.driver.switch_to_default_content()
		# frames = self.driver.find_elements_by_tag_name('frame')
		# Click the "Schedule Exams button"
		self.driver.switch_to_frame("WrapSignInNavMenuFrame")
		timeEle = self.driver.find_element_by_xpath("//table[@id = 'web2NavLayer']/tbody/tr[2]/td/a")
		timeEle.click()

		time.sleep(5)
		self.driver.switch_to_default_content()
		self.driver.switch_to_frame("appsFrame")
		self.driver.switch_to_frame("RegSchedPageFrame")
		checkEle = self.driver.find_element_by_name('param_examseries_checkbox_id0')
		checkEle.click()
		
		continueEle = self.driver.find_element_by_name('Continue')
		continueEle.click()

	def endInstance(self):
		self.driver.close()

if __name__ == "__main__":
	userName = "lihan0086"
	passWord = "Woaixieshiyi1314"
	instance = WebInstance(userName, passWord, True)
	instance.startInstance()
	instance.processInstance()