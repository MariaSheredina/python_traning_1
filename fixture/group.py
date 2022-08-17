# урок3_2
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create_group(self, group):
        wd = self.app.wd
        self.app.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.app.return_group_page()

    def fill_group_form(self, group):
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def del_first_group(self):
        wd = self.app.wd
        self.app.open_group_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()

    def edit_first_group(self, new_name):
        wd = self.app.wd
        self.app.open_group_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # edit
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(new_name)
        # submit group
        wd.find_element_by_name("update").click()
        self.app.return_group_page()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.app.open_group_page()
        self.select_first_group()
        # open modification form
        wd.find_element_by_name("edit").clear()
        # fill group form
        self.fill_group_form(group)
        # submit modification
        wd.find_element_by_name("update").clear()
        self.app.return_group_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
