# задание10
# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contact(app):
    app.contact.create_contact(Contact(firstname="Кто", middlename="Кто-кто", lastname="Кто-то", nickname="Mari", company="Company", address="NNovgorod", mobile="9200000000"))
