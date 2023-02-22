import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class SignUp(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_failed_register(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        driver.find_element(By.ID, "signUp").click()
        time.sleep(1)
        driver.find_element(By.ID, "name_register").send_keys("luthfi")
        time.sleep(1)
        driver.find_element(By.ID, "email_register").send_keys("luthfi@gmail.com")
        time.sleep(1)
        driver.find_element(By.ID, "password_register").send_keys("Password#1")
        time.sleep(1)
        driver.find_element(By.ID, "signup_register").click()
        time.sleep(1)


    # validasi
        response_data = driver.find_element(By.ID,"swal2-content").text
        self.assertIn('Gagal Register!', response_data)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()