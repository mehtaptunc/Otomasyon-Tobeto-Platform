from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.common.keys import Keys
import pytest
import openpyxl
from constants import globalConstants as c


#Test Senaryosu 1 Adı : Giriş Paneli Kontrolü
#Case 1 : Başarılı Giriş Kontrolü


class Test_Tobeto_Platform_Login_Test:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(c.BASE_URL)
        self.driver.maximize_window()

    def teardown_method(self): 
        self.driver.quit()

    @pytest.mark.parametrize("email, password", [("kojacer986@vasteron.com", "deneme123")])
    def test_successful_login(self, email, password):
        emailInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, c.EMAIL_XPATH)))
        emailInput.send_keys(email)
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, c.PASSWORD_XPATH)))
        passwordInput.send_keys(password)
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, c.LOGIN_BUTTON_XPATH)))
        loginButton.click()
        systemMessage = WebDriverWait(self.driver,5).until(ec.presence_of_element_located((By.XPATH, c.SYSTEM_SUCCESSFUL_MESSAGE)))
        assert systemMessage.text == "• Giriş başarılı."  
    


    #Case 2 : E-posta veya Şifre Girilmediğinde
    @pytest.mark.parametrize("email, password", [("", ""), ("kojacer986@vasteron.com", ""),("", "test123")])
    def test_passing_empty(self, email, password):
        emailInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.EMAIL_XPATH)))
        emailInput.send_keys(email)
        passwordInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.PASSWORD_XPATH)))
        passwordInput.send_keys(password)
        loginButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.LOGIN_BUTTON_XPATH)))
        loginButton.click()
        errorMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.ERROR_MESSAGE_XPATH)))
        assert errorMessage.text == "Doldurulması zorunlu alan*"
       
    #Case 3 :  E-posta veya Şifre Hatalı Girildiğinde
    @pytest.mark.parametrize("email, password", [("fffffg@.com", "475133"), ("kojacer986@.com", "1237"),("45512@gmail.com", "test123")])
    def test_false_login(self, email, password):
        emailInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.EMAIL_XPATH)))
        emailInput.send_keys(email)
        passwordInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.PASSWORD_XPATH)))
        passwordInput.send_keys(password)
        loginButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.LOGIN_BUTTON_XPATH)))
        loginButton.click()    
        errorMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div[class='toast-body']")))
        assert errorMessage.text== "• Geçersiz e-posta veya şifre."