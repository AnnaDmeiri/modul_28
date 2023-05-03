from selenium.webdriver.common.by import By
from pages.Base_page import BasePage
from config import TestData

class MainPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)


    MAIN_LOGO = (By.CSS_SELECTOR, "#app-header > div > div > svg")
    MAIL = (By.XPATH, "//*[@id='t-btn-tab-mail']")
    USERNAME = (By.XPATH, '// *[ @ id = "username"]')
    PASS = (By.XPATH, '//*[@id="password"]')
    BUTTON_INPUT = (By.XPATH, '//*[@id="kc-login"]')
    BUTTON_LOGOUT = (By.CSS_SELECTOR, "#logout-btn")
    ERROR_USERNAME_PASS = (By.XPATH, '// *[ @ id = "form-error-message"]')
    FORGOT = (By.CSS_SELECTOR, "#forgot_password")
    PAGE_RIGHT = (By.XPATH, '//*[@id="page-right"]/div/div/h1')
    BACK_BUTTON = (By.XPATH, '//*[@id="reset-back"]')
    REGISTER = (By.XPATH, '// *[ @ id = "kc-register"]')
    NAME = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input')
    SURNAME = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input')
    REGION = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/div/input')
    EMAIL = (By.XPATH, '//*[@id="address"]')
    PASSWORD = (By.XPATH, '//*[@id="password"]')
    PASSWORD_REPEAT = (By.XPATH, '//*[@id="password-confirm"]')
    BUTTON_REGISTER = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/button')
    ERROR_HINT_EMAIL = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/span')
    ERROR_HINT_NAME = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span')
    VK = (By.CSS_SELECTOR, '#oidc_vk>svg')




# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
