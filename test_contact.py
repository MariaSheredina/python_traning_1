# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_metod(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_contact_page(wd)
        self.create_contact(wd, Contact(firstname="Maria", middlename="Victorovna", lastname="Sidorova",
                                        nickname="Mari", company="Company", address="NNovgorod",
                                        mobile="9200150025", bday="5", bmonth="12", byear="2000"))
        self.return_to_group_page(wd)
        self.logout(wd)

-----------------------------------------------------------------------



    def open_home_page(self, wd):
        wd.get("https://localhost/addressbook/edit.php")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_group_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def create_contact(self, wd, contact):
        # init contact creation
        wd.find_element_by_name("new").click()
        # fill contact form
        wb.find_element_by_name("firstname").click()
        wb.find_element_by_name("firstname").clear()
        wb.find_element_by_name("firstname").send_keys(contact.firstname)
        wb.find_element_by_name("middlename").click()
        wb.find_element_by_name("middlename").clear()
        wb.find_element_by_name("middlename").send_keys(contact.middlename)
        wb.find_element_by_name("lastname").click()
        wb.find_element_by_name("lastname").clear()
        wb.find_element_by_name("lastname").send_keys(contact.lastname)
        wb.find_element_by_name("nickname").click()
        wb.find_element_by_name("nickname").clear()
        wb.find_element_by_name("nickname").send_keys(contact.nickname)
        wb.find_element_by_name("title").click()
        wb.find_element_by_name("company").click()
        wb.find_element_by_name("company").clear()
        wb.find_element_by_name("company").send_keys(contact.company)
        wb.find_element_by_name("address").click()
        wb.find_element_by_name("address").clear()
        wb.find_element_by_name("address").send_keys(contact.address)
        wb.find_element_by_name("mobile").click()
        wb.find_element_by_name("mobile").clear()
        wb.find_element_by_name("mobile").send_keys(contact.mobile)
        wb.find_element_by_name("work").click()
        wb.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wb.find_element_by_xpath("//option[@value='4']").click()
        wb.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wb.find_element_by_xpath("//option[@value='December']").click()
        wb.find_element_by_name("byear").click()
        wb.find_element_by_name("byear").clear()
        wb.find_element_by_name("byear").send_keys(contact.byear)
        wb.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        # submit contact creation
        wd.find_element_by_name("submit").click()


    def return_to_add_new_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def logout(self, wd):
         wd.find_element_by_link_text("Logout").click()

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
