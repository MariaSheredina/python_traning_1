# задание10


class OpenHelper:
    def __init__(self, app):
        self.app = app

    def open_book(self):
        wd = self.app.wd
        wd.get("https://localhost/addressbook")

    def groups_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0:
            wd.find_element_by_link_text("groups").click()

    def return_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def contact_page(self):
        wd = self.app.wd
        # if not wd.current_url.endswith("/contact.php") and len(wd.find_elements_by_name("enter")) > 0:
        wd.find_element_by_link_text("add new").click()

    def home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
