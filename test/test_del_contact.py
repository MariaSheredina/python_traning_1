# push_задание7
# -*- coding: utf-8 -*-

def test_del_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.del_first_contact()
    # wd.switch_to.alert.accept() подтверждение удаления контакта
    app.session.logout()
