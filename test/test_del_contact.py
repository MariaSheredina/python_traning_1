# задание9
# -*- coding: utf-8 -*-
from model.contact import Contact


def test_del_contact(app):
    if app.contact.count_contact == 0:
        app.contact.create_contact(Contact(firstname="Maria"))
    app.contact.del_first_contact()
