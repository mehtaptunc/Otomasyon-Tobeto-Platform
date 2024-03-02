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


class Test_Tobeto_Platform_Password_Forget:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(c.PASSWORD_FORGET_URL)
        self.driver.maximize_window()

    def teardown_method(self): 
        self.driver.quit()
   
    
    #Case 1: Şifre sıfırlama e-postası gönderme.
    def test_password_forget(self):
        emailInput=WebDriverWait(self.driver,5).until(ec.presence_of_element_located((By.CSS_SELECTOR,"#__next > div > main > section > div > div > div > input")))   
        emailInput.send_keys("kojacer986@vasteron.com")
        sendButton=WebDriverWait(self.driver,5).until(ec.presence_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div/button"))) 
        sendButton.click()
    
        errorMessage=WebDriverWait(self.driver,2).until(ec.presence_of_element_located((By.XPATH, c.FORGET_ERROR_MESSAGE_XPATH)))
        assert errorMessage.text=="• Şifre sıfırlama linkini e-posta adresinize gönderdik. Lütfen gelen kutunuzu kontrol edin."
        self.driver.save_screenshot("screenshotPhoto./sifresıfırlama.png") 
   
    #Case 2: Geçersiz e-postası gönderme.
    def test_invalid_password(self):  
        emailInput=WebDriverWait(self.driver,5).until(ec.presence_of_element_located((By.CSS_SELECTOR,"#__next > div > main > section > div > div > div > input")))   
        emailInput.send_keys("sxhahxabsch")
        sendButton=WebDriverWait(self.driver,5).until(ec.presence_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div/button"))) 
        sendButton.click()
        errorMessage=WebDriverWait(self.driver,2).until(ec.presence_of_element_located((By.XPATH," //*[@id='__next']/div/main/div[2]/div/div[2]")))
        #assert errorMessage.text=="Girdiğiniz e-posta geçersizdir"
        assert "Girdiğiniz e-posta geçersizdir" in errorMessage.text 
        self.driver.save_screenshot("screenshotPhoto./sifrehata.png") 
       
        #ekran görüntüsünü alır. dosya konumu bizim çalıştığımız dosya konumu yaptık