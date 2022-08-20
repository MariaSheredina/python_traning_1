# задание9
# -*- coding: utf-8 -*-

def test_modify_contact_lastname(app):
    if app.contact.count_contact() == 0:
        app.contact.create_contact(lastname="Bu")
    app.contact.modify_first_contact(lastname="Bbu")


def test_modify_contact_address(app):
    if app.contact.count_contact() == 0:
        app.contact.create_contact(address="NNovgorod")
    app.contact.modify_first_contact(address="Saint Petersburg")
