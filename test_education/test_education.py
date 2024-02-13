from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.common.keys import Keys
import pytest
from constants import globalConstants as c
from selenium.webdriver.common.action_chains import ActionChains



class Test_Tobeto_Platform_Edication:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(c.BASE_URL)
        self.driver.maximize_window()

    def teardown_method(self): 
        self.driver.quit()
   
   
    def valid_login_method(self,email,password):
        emailInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, c.EMAIL_XPATH)))
        emailInput.send_keys(email)
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, c.PASSWORD_XPATH)))
        passwordInput.send_keys(password)
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, c.LOGIN_BUTTON_XPATH)))
        loginButton.click()  
        sleep(5)
    
    # Case 1: Eğitimlere başarılı giriş
    def test_my_courses(self):
        self.valid_login_method("mehtapttunc@gmail.com","******")
        sleep(3)
        self.driver.execute_script("window.scrollBy(0, 500);")
        sleep(2)
        myEducation= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//button[@id='lessons-tab']")))
        sleep(3)
        myEducation.click()
        sleep(4)
        showMore= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div[class='row mt-3'] div[class='showMoreBtn']")))
        showMore.click()
        sleep(3)
        current_url = self.driver.current_url
        expected_url ="https://tobeto.com/egitimlerim"
        assert current_url == expected_url  
        
    # Case 2: Ecmel Ayral'dan  Hoşgeldin Mesajı 
    def test_wolcome_control(self):     
        self.valid_login_method("mehtapttunc@gmail.com","******")
        self.driver.execute_script("window.scrollBy(0, 500);")
        myEducation= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//button[@id='lessons-tab']")))
        sleep(3)
        myEducation.click()
        goEducation= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='all-lessons-tab-pane']/div/div[1]/div/div[2]/a")))
        sleep(3)
        goEducation.click()
        sleep(7)
        welcomeMessage= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='activity-unit-detail']/div/div[1]/div[1]/div"))) 
        assert welcomeMessage.text == "Dr. Ecmel Ayral'dan Hoşgeldin Mesajı"
    
    
       