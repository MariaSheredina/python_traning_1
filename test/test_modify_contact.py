# задание13
# -*- coding: utf-8 -*-

from model.contact import Contact
from random import randrange


def test_modify_contact_lastname(app):
    if app.contact.count_contact() == 0:
        app.contact.create_contact(Contact(firstname="Maria"))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    contact = Contact(firstname="Marina")
    contact.id = old_contact[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[index] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
