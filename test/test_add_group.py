# исправление для заданий 7,8
# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contact(app):
    app.contact.create_contact(Contact(firstname="Maria", middlename="Vi", lastname="Bu", nickname="Mari", company="Company", address="NNovgorod", mobile="9200000000"))


