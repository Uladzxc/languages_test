import time
from selenium.webdriver.common.by import By


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class Test_Catalogue:

    def test_button_add_to_basket_is_visible(self, browser):

        browser.get(link)

        time.sleep(5)

        add_button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        assert add_button.is_displayed()