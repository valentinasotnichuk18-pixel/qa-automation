from selenium.webdriver.common.by import By
from pages.base_page import BasePage    
class LoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login button")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".flash.success")   
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".flash.error")
    def open_login_page(self):
        self.driver.get(self.URL)   
    def enter_username(self, username):
        self.type(self.USERNAME_INPUT, username)    
    def enter_password(self, password):
        self.type(self.PASSWORD_INPUT, password)
    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)   
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
    def is_success_message_visible(self):
        return self.is_visible(self.SUCCESS_MESSAGE)
    def is_error_message_visible(self):
        return self.is_visible(self.ERROR_MESSAGE)  