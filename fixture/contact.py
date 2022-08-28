# задание11
# -*- coding: utf-8 -*-

from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_contact(self, contact):
        wd = self.app.wd
        self.app.open.contact_page()
        self.fill_contact_form(contact)
        wd.find_element_by_name("submit").click()
        self.app.open.contact_page()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.mobile)

    def del_first_contact(self):
        wd = self.app.wd
        self.app.open.home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.open.home_page()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.app.open.home_page()
        self.select_first_contact()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.app.open.home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def count_contact(self):
        wd = self.app.wd
        self.app.open.home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.app.open.contact_page()
        list_contact = []
        for element in wd.find_elements_by_css_selector("span.contact"):
            # span.contact возможно по-другому называется
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            # "selected[]" и "value" возможно по-другому называются
            list_contact.append(Contact(firstname=text, id=id))
        return list_contact
