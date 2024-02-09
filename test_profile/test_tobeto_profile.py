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
from selenium.webdriver.common.action_chains import ActionChains


class Test_Tobeto_Platform_Information_Profilo:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(c.BASE_URL)
        self.driver.maximize_window()

    def teardown_method(self): 
        self.driver.quit()
    
    
    @pytest.mark.parametrize("email, password", [("kojacer986@vasteron.com", "deneme123")])
    def profile_method(self,email,password):
        emailInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, c.EMAIL_XPATH)))
        emailInput.send_keys(email)
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, c.PASSWORD_XPATH)))
        passwordInput.send_keys(password)
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, c.LOGIN_BUTTON_XPATH)))
        loginButton.click()  
        sleep(5)
        self.driver.execute_script("window.scrollBy(0, 370);")
        sleep(5)
        
        startButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
        startButton.click()
        sleep(5)
       

    #Case 1 :  Profil başlıklarının  kontrolü (Kişisel bilgilerim )
    def test_profile_title_control1(self):
        email = "kojacer986@vasteron.com"
        password = "deneme123"
        self.profile_method(email,password)
        current_url = self.driver.current_url
        expected_url = "https://tobeto.com/profilim/profilimi-duzenle/kisisel-bilgilerim"
        assert current_url == expected_url
    
    
    #Case 2:  Profil başlıklarının  kontrolü (Deneyimlerim ) 
    def test_profile_title_control2(self):
        email = "kojacer986@vasteron.com"
        password = "deneme123"
        self.profile_method(email,password)
        experience=  WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[2]/span[2]")))
        experience.click()
        current_url = self.driver.current_url
        expected_url = "https://tobeto.com/profilim/profilimi-duzenle/deneyimlerim"
        assert current_url == expected_url    

    #Case 3:  Profil başlıklarının  kontrolü (Yetkinliklerim )
    def test_profile_title_control3(self):
        email = "kojacer986@vasteron.com"
        password = "deneme123"
        self.profile_method(email,password)
        competence= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[4]/span[2]")))
        competence.click()
        current_url = self.driver.current_url
        expected_url = "https://tobeto.com/profilim/profilimi-duzenle/yetkinliklerim"
        assert current_url == expected_url           

    
    #Case 4: Kişisel Bilgilerin Başarısız Girilmesi kontrolü  
    def test_profile_failed_check(self):
        email = "kojacer986@vasteron.com"
        password = "deneme123"
        self.profile_method(email,password)
     
        birhtDate= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,"birthday"))) 
        birhtDate.send_keys("12.01.1990")
        identifier=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,"identifier"))) 
        identifier.send_keys("54545455551")
        country= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,"country")))
        country.send_keys("Türkiye")
        city= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,"city")))
        city.send_keys("İstanbul")
        district= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[10]/select")))
        sleep(2)
        district.send_keys("Ümraniye")
        address= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,"address")))
        sleep(2)
        self.driver.execute_script("window.scrollBy(0, 150);")
        address.send_keys("Deneme mah.")
        description= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"textarea[placeholder='Kendini kısaca tanıt']")))
        description.send_keys("Denemen sjdnhdshshchsdchschsdjsjc")
        saveButton= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/button")))
        saveButton.click()
        errorMessage= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/div[2]/div/div[2]"))) 
        assert errorMessage.text=="• Kimlik bilgilerinizi hatalı girdiniz."
    
    
    #Case 5:  Profil resmi ekle kontrolü

    def test_add_profile_picture(self):
        email = "kojacer986@vasteron.com"
        password = "deneme123"
        self.profile_method(email,password)
        photo= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,".photo-edit-btn.cursor-pointer")))
        photo.click()
        box= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[2]")))
        assert box.is_displayed