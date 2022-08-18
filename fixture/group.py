# урок3_2
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create_group(self, group):
        wd = self.app.wd
        self.app.open.group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.app.open.return_group_page()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.app.open.group_page()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        wd.find_element_by_name("update").click()
        self.app.open.return_group_page()

    def del_first_group(self):
        wd = self.app.wd
        self.app.open.group_page()
        self.select_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()

    def edit_first_group(self, new_name):
        wd = self.app.wd
        self.app.open.group_page()
        self.select_first_group()
        # edit
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(new_name)
        # submit group
        wd.find_element_by_name("update").click()
        self.app.open.return_group_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
