# задание9
# -*- coding: utf-8 -*-

from model.contact import Contact


def test_modify_contact_lastcontact(app):
    if app.contact.count_contact == 0:
        app.contact.create_contact(Contact(lastname="Bu"))
    app.contact.modify_first_contact(Contact(lastname="Bbu"))


# def test_modify_contact_address(app):
    # if app.contact.count_contact == 0:
        # app.contact.create_contact(Contact(address="NNovgorod"))
    # app.contact.modify_first_contact(Contact(address="Saint Petersburg"))
