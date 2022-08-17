# push_задание7
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_book(self):
        wd = self.wd
        wd.get("https://localhost/addressbook")

    def open_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def return_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def open_contact_page(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def open_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()

    def return_contact_page(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def dectroy(self):
        self.wd.quit()
