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


class Test_Tobeto_Platform_MyAnnouncement_And_News:

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
   
   #Case 1 : Duyuru ve Haberlerim kısmına erişim kontrolü
    def test_announceAndNews(self):    
        self.valid_login_method("mehtapttunc@gmail.com","********")
        sleep(3)
        self.driver.execute_script("window.scrollBy(0, 150);") 
        sleep(3)   
        announcementAndNewsButton= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//button[@id='notification-tab']")))
        announcementAndNewsButton.click()
        newsView= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='notification-tab-pane']/div")))
        newsView.is_displayed 
    
    #Case 2 : Duyuru ve Haberlerim kısmı 9 modüllerin görüntülenebilmesi
    def test_show_more(self):      
        self.valid_login_method("mehtapttunc@gmail.com","*******")
        sleep(3)
        self.driver.execute_script("window.scrollBy(0, 150);") 
        sleep(3)   
        announcementAndNewsButton= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//button[@id='notification-tab']")))
        announcementAndNewsButton.click()
        self.driver.execute_script("window.scrollBy(0, 200);") 
        sleep(3)
        showmoreButton= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='notification-tab-pane']/div/div[4]")))
        sleep(2)
        showmoreButton.click()
        sleep(3)
        modüller = WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.CSS_SELECTOR, "[class='col-md-4 col-12 my-4']")))
        assert len(modüller) == 9 
      
       
           
