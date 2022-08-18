# урок3_2
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create_group(self, group):
        wd = self.app.wd
        self.app.open.group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.app.open.group_page()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if group.name is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def del_first_group(self):
        wd = self.app.wd
        self.app.open.group_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()

    def edit_first_group(self, new_name):
        wd = self.app.wd
        self.app.open.open_group_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # edit
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(new_name)
        # submit group
        wd.find_element_by_name("update").click()
        self.app.open.group_page()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.app.open.open_group_page()
        self.select_first_group()
        # open modification form
        wd.find_element_by_name("edit").clear()
        # fill group form
        self.fill_group_form(self, group)
        # submit modification
        wd.find_element_by_name("update").clear()
        self.app.open.group_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
