import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

web_domain = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

class AdminJobTitles(unittest.TestCase) :

    def setUp(self) :
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def login(self) :
        # OPEN BROWSER
        driver = self.browser
        driver.get(web_domain)
        time.sleep(3)
        driver.maximize_window()
        time.sleep(1)

        # LOGIN
        driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(1)
    
    def gotoAdminJobTitlesPage(self) :
        driver = self.browser

        driver.find_element(By.XPATH, "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[1]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[contains(text(),'Job ')]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[contains(text(),'Job Titles')]").click()
        time.sleep(3)

    def test_TC001(self) :
        driver = self.browser
        self.login()
        self.gotoAdminJobTitlesPage()

        # VALIDASI
        jobTitlesHeader = driver.find_element(By.XPATH, "//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title']").text
        self.assertIn("Job Titles", jobTitlesHeader)

    def test_TC002(self) :
        driver = self.browser
        self.login()
        self.gotoAdminJobTitlesPage()

        # STEP
        trashIcon = driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-trash'])[1]")
        trashIcon.click()
        time.sleep(1)

        yesDeleteButton = driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-trash oxd-button-icon']")
        yesDeleteButton.click()
        time.sleep(3)

        # VALIDASI
        jobTitlesHeader = driver.find_element(By.XPATH, "//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title']").text
        self.assertIn("Job Titles", jobTitlesHeader)

    def test_TC003(self) :
        driver = self.browser
        self.login()
        self.gotoAdminJobTitlesPage()

        # STEP
        checkBoxItem = driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-check oxd-checkbox-input-icon'])[2]")
        checkBoxItem.click()
        time.sleep(1)

        # VALIDASI
        popDeleteButton = driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-trash-fill oxd-button-icon']")
        self.assertNotIn(0, popDeleteButton.size)       #Object Exist
        time.sleep(3)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__" :
    unittest.main()