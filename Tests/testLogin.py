import unittest
import os
from random import randint
from appium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

class LoginTests(unittest.TestCase):

    def setUp(self):
        # Update this to match the build .app location and the device info
        app = ('/Users/tourajvaziri/AppiumIOS/build/Release-iphonesimulator/AppiumTest.app')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '13.3',
                'deviceName': 'iPhone 8'
            }
        )

    def tearDown(self):
        self.driver.quit()

    def testEmailField(self):
        emailTF = self.driver.find_element_by_accessibility_id('emailTextField')
        emailTF.send_keys("touraj@Test.com")
        emailTF.send_keys(Keys.RETURN)
        sleep(1)
        self.assertEqual(emailTF.get_attribute("value"), "touraj@Test.com")

    def testPasswordField(self):
        passwordTF = self.driver.find_element_by_accessibility_id('passwordField')
        passwordTF.send_keys("touraj123")
        passwordTF.send_keys(Keys.RETURN)
        sleep(1)
        self.assertNotEqual(passwordTF.get_attribute("value"), "touraj123")

    def testLogin(self):
        self.testEmailField()
        self.testPasswordField()
        self.driver.find_element_by_accessibility_id('loginBtn').click()
        sleep(1)
        smiley = self.driver.find_element_by_accessibility_id('smileyImage')
        self.assertTrue(smiley.get_attribute('wdVisible'))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
