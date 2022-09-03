# задание11
# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contact(app):
    old_contact = app.contact.get_contact_list()
    contact = Contact(firstname="Иван", lastname="Иванов")
    app.contact.create_contact(contact)
    assert len(old_contact) + 1 == app.contact.count_contact()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
