import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class LoginFailed(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_login_failed(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)


    # validasi
        objectData = driver.find_element(By.XPATH, '//div[@class="error-message-container error"]')
        self.assertNotIn(0, objectData.size)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()