# задание11
# -*- coding: utf-8 -*-

from model.contact import Contact


def test_modify_contact_lastname(app):
    if app.contact.count_contact() == 0:
        app.contact.create_contact(Contact(firstname="Maria"))
    old_contact = app.contact.get_contact_list()
    contact = Contact(firstname="Marina")
    contact.id = old_contact[0].id
    app.contact.modify_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
