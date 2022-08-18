import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .page_elements import PageElements
from configurations.test_data import WeatherAppTestData
from inspect import signature

# Instianting Page Element class
ui_elements = PageElements()

# Instianting Test data Class
test_data = WeatherAppTestData()


class WeatherAppFunctionality(BasePage):
    """Class describes test scripts for Functionality """
    
                
    def get_temperature_degrees(self):
        element = ui_elements.temp_xpath
        get_value = self.driver.find_element(By.XPATH, element).text
        return get_value
        # moisturizer_heading_txt = self.driver.find_element(By.XPATH, element).text
        # assert moisturizer_heading_txt == "Moisturizers"
        
    
    def get_least_expensive_aloe_product(self):
        buttons = self.driver.find_elements_by_xpath("//button[.='Add']")
        price = []
        for button in buttons:
            onclick_text = button.get_attribute('onclick')
       
            if "Aloe" in onclick_text :
                x = onclick_text.split(",")[1][:-1]
                price.append(x)
                if min(price):
                    button.click()     
                    
    def add_product_cart(self):
        element = ui_elements.add_button_xpath
       
        add_button = self.driver.find_element(By.XPATH,
                                                element)
        self.driver.execute_script("arguments[0].click();",
                                   add_button)
        
    def click_cart(self):
        element = ui_elements.cart_button_xpath
        cart_button = self.driver.find_element(By.XPATH,
                                                element)
        self.driver.execute_script("arguments[0].click();",
                                   cart_button)
        
    def click_pay_with_card_button(self):
        element = ui_elements.pay_card_xpath
        pay_button = self.driver.find_element(By.XPATH,
                                                element)
        self.driver.execute_script("arguments[0].click();",
                                   pay_button)
        
    def input_email(self):
        element = ui_elements.card_email_xpath
        email = test_data.email
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name('iframe'))
        # self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_xpath(element)
        self.driver.find_element(By.XPATH, element).clear()
        self.driver.find_element(By.XPATH, element).send_keys(email)
        
    def input_card_number(self):
        element = ui_elements.card_number_xpath
        card = test_data.card_number
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name('iframe'))
        self.driver.find_element_by_xpath(element)
        self.driver.find_element(By.XPATH, element).clear()
        self.driver.find_element(By.XPATH, element).send_keys(card)
        
    def input_date(self):
        element = ui_elements.date_xpath
        date = test_data.date
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name('iframe'))
        self.driver.find_element(By.XPATH, element).clear()
        self.driver.find_element(By.XPATH, element).send_keys(date)
        
    def input_cvc(self):
        element = ui_elements.cvc_xpath
        cvc = test_data.cvc
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name('iframe'))
        self.driver.find_element(By.XPATH, element).clear()
        self.driver.find_element(By.XPATH, element).send_keys(cvc)
        
         
        
                
        
        
    
    
    