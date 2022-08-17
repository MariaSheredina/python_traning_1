# push_задание7
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.accept_next_alert = True

    def open_book(self):
        wd = self.wd
        wd.get("https://localhost/addressbook")

    def is_element_present(self, how, what):
        try: self.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def dectroy(self):
        self.wd.quit()
