import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Login(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_login_success(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        driver.find_element(By.ID, "signUp").click()
        time.sleep(1)
        driver.find_element(By.ID, "email").send_keys("luthfi@gmail.com")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("password1")
        time.sleep(1)
        driver.find_element(By.ID, "signin_login").click()
        time.sleep(1)


    # validasi
        response_data = driver.find_element(By.ID,"swal2-content").text
        self.assertIn('Anda Berhasil Login', response_data)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()