# задание13
# -*- coding: utf-8 -*-

from model.contact import Contact
import re


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
        # self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        # self.change_field_value("nickname", contact.nickname)
        # self.change_field_value("company", contact.company)
        # self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("phone2", contact.secondaryphone)
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

    # def modify_first_contact(self):
        # self.modify_contact_by_index(0)

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
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                firstname = cells[1].text
                lastname = cells[2].text
                all_phones = cells[5].text
                # all_phones = cells[5].text.splitlines()
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname, all_phones_from_home_page=all_phones))
                # homephone=all_phones[0], mobilephone=all_phones[1], workphone=all_phones[2], secondaryphone=all_phones[3]
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open.home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open.home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, homephone=homephone,
                       mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone, id=id)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone)
