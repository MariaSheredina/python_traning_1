# урок3_3

class OpenHelper:
    def __init__(self, app):
        self.app = app

    def open_book(self):
        wd = self.app.wd
        wd.get("https://localhost/addressbook")

    def groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def return_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
