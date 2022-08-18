from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .page_elements import PageElements

# Instianting OverViewElement
ui_elements = PageElements()


class UiChecks(BasePage):
    """Class describes test scripts for Ui checks"""

    # check labels
    def check_homepage_heading_label(self):
        element = ui_elements.homepage_header_xpath
        self.driver.find_element(By.XPATH, element).is_displayed()
        homepage_heading_txt = self.driver.find_element(By.XPATH, element).text
        assert homepage_heading_txt == "Current temperature"
        
    def check_moisturizer_heading_label(self):
        element = ui_elements.moisturizer_header_xpath
        self.driver.find_element(By.XPATH, element).is_displayed()
        moisturizer_heading_txt = self.driver.find_element(By.XPATH, element).text
        assert moisturizer_heading_txt == "Moisturizers"
        
    def check_moisturizer_button(self):
        element = ui_elements.buy_moisturizer_button
        self.driver.find_element_by_xpath(element).is_displayed()
        self.driver.find_element_by_xpath(element).is_enabled()
        
    def click_moisturizer_button(self):
        element = ui_elements.buy_moisturizer_button
        moisturizer_button = self.driver.find_element(By.XPATH,
                                                element)
        self.driver.execute_script("arguments[0].click();",
                                   moisturizer_button)
        
    def check_sunscreens_heading_label(self):
        element = ui_elements.sunscreen_header_xpath
        self.driver.find_element(By.XPATH, element).is_displayed()
        sunscreens_heading_txt = self.driver.find_element(By.XPATH, element).text
        assert sunscreens_heading_txt == "Sunscreens"
        
    def check_moisturizer_page_heading_label(self):
        element = ui_elements.moisturizers_heading_page
        self.driver.find_element(By.XPATH, element).is_displayed()
        moisturizer_heading_txt = self.driver.find_element(By.XPATH, element).text
        assert moisturizer_heading_txt == "Moisturizers"
        
    def check_add_button(self):
        element = ui_elements.add_button_xpath
        self.driver.find_element_by_xpath(element).is_displayed()
        self.driver.find_element_by_xpath(element).is_enabled()
    
    def check_cart_button(self):
        element = ui_elements.cart_button_xpath
        self.driver.find_element_by_xpath(element).is_displayed()
        self.driver.find_element_by_xpath(element).is_enabled()  
        
    def check_sunscreen_button(self):
        element = ui_elements.buy_sunscreen_button
        self.driver.find_element_by_xpath(element).is_displayed()
        self.driver.find_element_by_xpath(element).is_enabled()
        
            
    def click_sunscreen_button(self):
        element = ui_elements.buy_sunscreen_button
        moisturizer_button = self.driver.find_element(By.XPATH,
                                                element)
        self.driver.execute_script("arguments[0].click();",
                                   moisturizer_button)
        
    def check_sunscreen_page_heading_label(self):
        element = ui_elements.sunscreen_heading_page
        self.driver.find_element(By.XPATH, element).is_displayed()
        moisturizer_heading_txt = self.driver.find_element(By.XPATH, element).text
        assert moisturizer_heading_txt == "Sunscreens"
        
    def check_add_button_sunscreen(self):
        element = ui_elements.sunscreen_add_button_xpath
        self.driver.find_element_by_xpath(element).is_displayed()
        self.driver.find_element_by_xpath(element).is_enabled()
    