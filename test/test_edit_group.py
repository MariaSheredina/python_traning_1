# push_задание7
# -*- coding: utf-8 -*-

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(new_name="qqq")
    app.session.logout()
