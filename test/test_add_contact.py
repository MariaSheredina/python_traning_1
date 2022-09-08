# задание15
# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_mobile():
    a = random.randrange(9000000000, 9999999999, 1)
    return a

def random_homephone():
    a = random.randrange(1000000, 9999999, 1)
    return a


testdata = [
    Contact(firstname=firstname, lastname=lastname, address=address, mobilephone=mobilephone)
    for firstname in ["", random_string("Firstname", 10)]
    for lastname in ["", random_string("Lastname", 20)]
    for address in ["", random_string("address", 20)]
    for homephone in ["", random_homephone()]
    for mobilephone in ["", random_mobile()]
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_contact(app, contact):
    old_contact = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    assert len(old_contact) + 1 == app.contact.count_contact()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
