
import pytest
import time
from selenium.common.exceptions import NoSuchElementException
from configurations.test_data import WeatherAppTestData
from utilities.custom_logger import LogGen
from page_objects.uichecks import UiChecks
from page_objects.functionality import WeatherAppFunctionality
from test_cases.configtest import setup

base_url = WeatherAppTestData.base_url
logger = LogGen.loggen()


class TestWeatherAppUichecks:
    """Class describes the methods to test cases for Weather Application Uichecks"""

    def test__moisturizer_uichecks(self, setup):
        """This methods tests uichecks of the application (moisturizer side)"""

        self.driver = setup
        self.driver.get(base_url)
        logger.info("**********Home Page*******")
        logger.info("*************Test Case  001**********************")

        
        #instatianting the page object class
        home_page = UiChecks(self.driver)
        
        page_title = self.driver.title
        if page_title == WeatherAppTestData.home_page_title:
            home_page.check_homepage_heading_label()
            home_page.check_moisturizer_heading_label()
            home_page.check_moisturizer_button()
            home_page.click_moisturizer_button()
            home_page.check_moisturizer_page_heading_label()
            home_page.check_add_button()
            home_page.check_cart_button()
        else:
            logger.error("***Uichecks Fialed***")
            self.driver.save_screenshot("../screenshots/test_weatherapp.png")
        self.driver.quit()
        
    
    def test__sunscreens_uichecks(self, setup):
        """This methods tests uichecks of the application(sunscreen side)"""

        self.driver = setup
        self.driver.get(base_url)
        logger.info("**********Home Page*******")
        logger.info("*************Test Case  001**********************")

        
        #instatianting the page object class
        home_page = UiChecks(self.driver)
        
        page_title = self.driver.title
        if page_title == WeatherAppTestData.home_page_title:
            home_page.check_homepage_heading_label()
            home_page.check_sunscreens_heading_label()
            home_page.check_sunscreen_button()
            home_page.click_sunscreen_button()
            home_page.check_sunscreen_page_heading_label()
            home_page.check_add_button_sunscreen()
            home_page.check_cart_button()
        else:
            logger.error("***Uichecks  Fialed***")
            self.driver.save_screenshot("../screenshots/test_weatherapp.png")
        self.driver.quit()
        
    
class TestWeatherAppFunctionality:
    """Class describes the methods to test cases for Weather Application Functionality"""

    def test_shop_moisturizers_functionality(self, setup):
        """This methods tests functionality of the application (moisturizer side)"""

        self.driver = setup
        self.driver.get(base_url)
        logger.info("**********Moisturizer Page*******")
        logger.info("*************Test Case  002**********************")

        
        #instatianting the page object class
        func_page = WeatherAppFunctionality(self.driver)
        
        home_page = UiChecks(self.driver)
        
        page_title = self.driver.title
        if page_title == WeatherAppTestData.home_page_title:
            
            # check if current temperature is less that 19 °C 
           if  func_page.get_temperature_degrees() < "19 °C": 
            
               home_page.click_moisturizer_button()
               func_page.get_least_expensive_aloe_product()
               func_page.add_product_cart()
               func_page.click_cart()
               func_page.click_pay_with_card_button()
               func_page.input_email()
               time.sleep(10)
            #    func_page.input_card_number()
               func_page.input_date()
               func_page.input_cvc()
               
           else:
               print(func_page.get_temperature_degrees())
               home_page.click_moisturizer_button()
               func_page.get_least_expensive_aloe_product()
               func_page.add_product_cart()
               func_page.click_cart()
               func_page.click_pay_with_card_button()
               
            #    time.sleep(15)
               func_page.input_email()
               time.sleep(10)
            #    func_page.input_card_number()
               func_page.input_date()
               func_page.input_cvc()
               
           
        else:
            logger.error("***Uichecks  Fialed***")
            self.driver.save_screenshot("../screenshots/test_weatherapp.png")
        # self.driver.quit()