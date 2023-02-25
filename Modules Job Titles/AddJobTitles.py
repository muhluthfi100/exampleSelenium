import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

web_domain = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

class AddJobTitles(unittest.TestCase) :

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

    def test_TC004(self) :
        driver = self.browser
        self.login()
        self.gotoAdminJobTitlesPage()

        # STEP
        addButton = driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
        addButton.click()
        time.sleep(1)
        
        # VALIDASI
        addTitle = driver.find_element(By.XPATH, "//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title']").text
        self.assertIn("Add Job Title", addTitle)
        time.sleep(3)

    def test_TC005(self) :
        driver = self.browser
        self.login()
        self.gotoAdminJobTitlesPage()

        # STEP
        addButton = driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
        addButton.click()
        time.sleep(1)

        submitButton = driver.find_element(By.XPATH, "//button[@type='submit']")
        submitButton.click()
        time.sleep(1)

        # VALIDASI
        errorRequiredField = driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']")
        self.assertNotIn(0, errorRequiredField.size)    #Object exist

    def test_TC006(self) :
        driver = self.browser
        self.login()
        self.gotoAdminJobTitlesPage()

        # STEP
        addButton = driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
        addButton.click()
        time.sleep(5)

        nameField = driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        nameField.send_keys("New Titles 2")
        time.sleep(1)

        submitButton = driver.find_element(By.XPATH, "//button[@type='submit']")
        submitButton.click()
        time.sleep(5)

        # VALIDASI
        redirectedPage = driver.find_element(By.XPATH, "//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title']").text
        self.assertIn("Job Titles", redirectedPage)


    def tearDown(self):
        self.browser.close()

if __name__ == "__main__" :
    unittest.main()