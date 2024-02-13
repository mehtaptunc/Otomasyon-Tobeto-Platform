from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.common.keys import Keys
import pytest
from constants import globalConstants as c



class Test_Tobeto_Platform_Calendar:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(c.BASE_URL)
        self.driver.maximize_window()

    def teardown_method(self): 
        self.driver.quit()




    def calendar_method(self):
        
        calendarButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.CALENDAR_BUTTON)))
        calendarButton.click()
        radioButton1=WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.NAME,"eventEnded")))
        radioButton1.click()
        radioButton2=WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.NAME,"eventContinue")))
        radioButton2.click()
        radioButton3=WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.NAME,"eventBuyed")))
        radioButton3.click()
        radioButton4=WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.NAME,"eventNotStarted")))
        radioButton4.click()
        sleep(2)
        

     #Case 1: Takvim başlığının gösterilmesi 
    def test_page_title_calendar(self):
        self.calendar_method()
        calendar_page_title = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div[4]/div/div/div[1]/span")))
        assert calendar_page_title.text == "Eğitim ve Etkinlik Takvimi", "Başlık 'Eğitim ve Etkinlik Takvimi' olarak bekleniyor."
    
    #Case 2: Filtresiz tüm eğitimlerin takvim üzerinde gösterilmesi  
    def test_alltraining_calendar(self):     
        self.calendar_method()
        calendarDetail=WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.CSS_SELECTOR,c.DETAİL_CSS)))
        calendarDetail.is_selected
    
   
    #Case 3:Eğitimlerin arama filtresinde kontrolü
    @pytest.mark.parametrize("education", [ (".net"),("mobil")])        
    def test_education_search(self,education):     
        self.calendar_method()
        educationInput=WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"search-event")))   
        educationInput.send_keys(education)  
        educationDetail=WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"[class='fc-scrollgrid  fc-scrollgrid-liquid']")))
        educationDetail.is_displayed
        
    #Case 4: Eğitmen arama filtresinin kontrolü
    @pytest.mark.parametrize("instructor", [("Engin Demiroğ"), ("Ahmet Çetinkaya"),("Gürkan İlişen")]) 
    def test_instructor_search(self,instructor):   
        self.calendar_method()
        instructorInput=WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"react-select-2-input"))) 
        instructorInput.send_keys(instructor)
        instructorDetail=WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div[4]/div/div/div[2]/div/div/div[2]/div"))) 
        instructorDetail.is_displayed


    #Case 5: Eğitmen ve eğitim arama filtrelerinin birlikte kontrolü    
    @pytest.mark.parametrize("instructor,education", [("Engin Demiroğ",".net"), ("Ahmet Çetinkaya",".net"),("Gürkan İlişen","Siber Güvenlik")]) 
    def test_instructor_education_search(self,instructor,education):   
        self.calendar_method()
        instructorInput=WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"react-select-2-input"))) 
        instructorInput.send_keys(instructor)
        educationInput=WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"search-event")))   
        educationInput.send_keys(education) 
        detail=WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.CSS_SELECTOR,c.DETAİL_CSS))) 
        detail.is_displayed    

        
       
     #Case 6: Yön oklarıyla tarihlerin  kontrolü
    def test_find_date(self):    
        calendarButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.CALENDAR_BUTTON)))
        calendarButton.click()
        rightDirection= WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div[4]/div/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/button[2]")))
        rightDirection.click()
        sleep(2)
        nextDate= WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div[4]/div/div/div[2]/div/div/div[2]/div/div[1]/div")))
        nextDate.click()
        nextDate.is_displayed
        sleep(2)
        week_button = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, "//button[@title='Hafta']")))
        week_button.click()
        week_button.is_displayed
        sleep(2)
        day_button =  WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,  "//button[@title='Gün']")))
        day_button.click()
        day_button.is_displayed
        sleep(2)

        
     #Case 7: Ay  seçiminde takvimin değişmesinin kontrolü
    def test_month_control(self):    
        calendarButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.CALENDAR_BUTTON)))
        calendarButton.click()
        monthButton= WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div[4]/div/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[3]/div/button[1]")))
        monthButton.click()
        sleep(2)
        monthDate= WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div[4]/div/div/div[2]/div/div/div[2]/div/div[1]/div")))
        monthDate.is_displayed    
     
     #Case 8: Takvim pop-up ‘nın kapatılmasının kontrolü    
    def test_calendar_close(self):    
        calendarButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.CALENDAR_BUTTON)))
        calendarButton.click()
        closeButton= WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div[4]/div/div/div[1]/button")))
        closeButton.click()
        sleep(3)
        
            
          