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


class Test_Tobeto_Platform_Register_Test:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(c.REGİSTER_URL)
        self.driver.maximize_window()

    def teardown_method(self): 
        self.driver.quit()

    def register(self, email, password, passwordAgain , phone):    
        name = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, c.NAME_NAME)))
        name.send_keys("Hilal")
        
        surname = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, c.SURNAME_NAME)))
        surname.send_keys("Koç")
    

        emailInput = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, c.EMAIL_NAME)))
        emailInput.send_keys(email)

        
        password1 = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, c.PASSWORD_NAME)))
        password1.send_keys(password)  
         
  
        againPassword = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, c.PSW_AGAIN_NAME)))
        againPassword.send_keys(passwordAgain)
    
        self.driver.execute_script("window.scrollBy(0, 100);")
        sleep(3)

        registerbutton = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.CSS_SELECTOR, c.REGISTER_BTN_CSS)))
        registerbutton.click()
        sleep(2)
       
        AcikRizaMetni = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, c.ACIK_RIZA_NAME)))
        AcikRizaMetni.click()
       
        uyeliksoz = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, c.UYELIK_NAME)))
        uyeliksoz.click()
        
        emailonay = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, c.EMAIL_CLICK_NAME)))
        emailonay.click()
        
        Aramaonay = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, c.ARAMA_CLICK_NAME)))
        Aramaonay.click()
        sleep(8)
        
        phoneNumber = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.ID, c.PHONE_ID)))
        phoneNumber.send_keys(phone)
       
        sleep(5)
        
       #Iframe'ler, bir web sayfası içinde başka bir web sayfasını yerleştirmek için kullanılan HTML öğeleridir.
      # Bu kod, Selenium WebDriver'a, etkileşimde bulunmak istediğiniz içeriğin bulunduğu iframe'e odaklanmasını söyler.
        iframe=self.driver.find_element(By.XPATH, c.IFRAME_XPATH )
        self.driver.switch_to.frame(iframe)
        sleep(2)
        captcha=self.driver.find_element(By.XPATH,c.CAPTCHA_XPATH)
        captcha.click()
        sleep(30)
        # Iframe'den çıkıp ana sayfaya geri dönün
        self.driver.switch_to.default_content()
        sleep(2)
        continueButton = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.XPATH, c.CONTINUE_BUTTON_XPATH)))
        continueButton.click()
    
    


    #Case 1 : Başarılı Kayıt Ol Kontrolü
    def test_successful_register(self):
        self.register("elciinz@vasteron.com", "123deneme", "123deneme", "5474587966")
        sleep (2)
        registerMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"span[class='success-payment-text']")))
        assert "Tobeto Platform'a kaydınız başarıyla gerçekleşti." in registerMessage.text 
 

    # Case 2: Girdiğiniz e posta adresi ile kayıtlı üyelik bulunmaktadır uyarısının alınması.
    def test_unsuccessful_register(self):
        self.register("kojacer986@vasteron.com", "deneme123", "deneme123", "5464522633")
        sleep (2)
        registerErrorMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CLASS_NAME,"toast-body")))
        assert "• Girdiğiniz e-posta adresi ile kayıtlı üyelik bulunmaktadır." in registerErrorMessage.text 
       
     
    #Case 3: Kayıt ol sırasında istenen telefon numarası  karakter kontrolü  
    def test_invalid_phone1(self):
        self.register("lisa986@vasteron.com","123deneme","123deneme","54645")
        invalidMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div[4]/div/div/div/div/div/label[4]/small/p")))
        assert invalidMessage.text == "En az 10 karakter girmelisiniz."
        sleep (2)
    


    def test_invalid_phone2(self):
        self.register("gazi986@vasteron.com","123deneme","123deneme","0000000000000")
        errorMessage= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div[4]/div/div/div/div/div/label[4]/small/p")))
        assert errorMessage.text == "En fazla 10 karakter girebilirsiniz." 
        sleep (2)
   


    #Case 4: Şifrenin karakter sayı kontrolü.
    def test_password_less_than6(self):
        self.register("gazi@gmail.com", "123", "123", "5068372511")
        errorMessage = WebDriverWait(self.driver,2).until(ec.presence_of_element_located((By.CLASS_NAME,"toast-body")))
        assert errorMessage.text == "• Şifreniz en az 6 karakterden oluşmalıdır."
        sleep(2)

    
    
    
    #Case 5 : Geçersiz E-posta kontrolü 
    @pytest.mark.parametrize("email", [("123"),("e"),("m.t")])    
    def test_invalid_email(self,email):
        emailInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.REGISTER_MAIL_XPATH)))
        emailInput.send_keys(email)
        sleep(2)
        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/div/form/p")
        assert errorMessage.text=="Geçersiz e-posta adresi*"
       

    #Case 6 : Şifre eşleşmeme kontrolü
    def test_password_match(self):
        self.register("mehtap@gmail.com","1234567","7654321","5068742395")    
        errorMessage = WebDriverWait(self.driver,5).until(ec.presence_of_element_located((By.CLASS_NAME, "toast-body")))
        assert errorMessage.text == "• Şifreler eşleşmedi"
        sleep(5)    

    #Case 7 : Girilen bilgilerde 2 farklı hatalı kısım doldurulduğunda 
    def test_two_error(self):
        self.register("kojacer986@vasteron.com","123","123","5068742395")    
        errorMessage = WebDriverWait(self.driver,2).until(ec.presence_of_element_located((By.CLASS_NAME, "toast-body")))
        assert "• 2 errors occurred" in errorMessage.text 
        sleep(5)  