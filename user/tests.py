from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest1:
    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome("C:\\seleniumserver\\chromedriver.exe")
        self.driver.maximize_window()

    def construction_company_login_tests(self):
        self.driver.get("http://127.0.0.1:8000/")
        wait = WebDriverWait(self.driver, 5)
        login_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'nav-link') and @href='/user/login/']")))
        login_link.click()
        
        username_field = wait.until(EC.presence_of_element_located((By.ID, "id_username")))
        username_field.send_keys("denizsailing")

        password_field = wait.until(EC.presence_of_element_located((By.ID, "id_password")))
        password_field.send_keys("Karabiga3517")
        
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-danger")
        self.driver.execute_script("arguments[0].click();", login_button)

    def tear_down(self):
        self.driver.close()

if __name__ == "__main__":
    test = LoginTest1()
    test.setup()
    test.construction_company_login_tests()
    test.tear_down()
