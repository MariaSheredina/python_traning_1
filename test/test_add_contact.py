# задание11
# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contact(app):
    old_contact = app.contact.get_contact_list()
    contact = Contact(firstname="Иван", lastname="Иванов")
    app.contact.create_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
