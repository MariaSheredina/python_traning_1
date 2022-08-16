# push_задание7
# -*- coding: utf-8 -*-

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(new_address="Moscow")
    app.session.logout()
