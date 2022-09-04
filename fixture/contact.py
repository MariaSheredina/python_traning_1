# задание13
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
        self.contact_cache = None

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
        # self.change_field_value("nickname", contact.nickname)
        # self.change_field_value("company", contact.company)
        # self.change_field_value("address", contact.address)
        # self.change_field_value("mobile", contact.mobile)
        # self.change_field_value("work", contact.work)
        # self.change_field_value("fax", contact.fax)
        # self.change_field_value("email", contact.email)
        # self.change_field_value("email2", contact.email2)
        # self.change_field_value("email3", contact.email3)
        # self.change_field_value("homepage", contact.homepage)
        # self.change_field_1_value("bday", contact.bday)
        # self.change_field_1_value("bmonth", contact.bmonth)
        # self.change_field_value("byear", contact.byear)
        # self.change_field_1_value("aday", contact.aday)
        # self.change_field_1_value("amonth", contact.amonth)
        # self.change_field_value("ayear", contact.ayear)
        # self.change_field_value("address2", contact.address2)
        # self.change_field_value("phone2", contact.phone2)
        # self.change_field_value("notes", contact.notes)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open.home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.open.home_page()
        self.contact_cache = None

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.app.open.home_page()
        self.select_contact_by_index(index)
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.app.open.home_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def del_first_contact(self):
        self.delete_contact_by_index(0)

    def count_contact(self):
        wd = self.app.wd
        self.app.open.home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open.home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                fn = cells[2].text
                ln = cells[1].text
                self.contact_cache.append(Contact(id=id, firstname=fn, lastname=ln))
        return list(self.contact_cache)
