# push_задание7
# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contact(app):
    app.contact.create_contact(Contact(firstname="Maria", middlename="Victorovna", lastname="Sidorova", nickname="Mari", company="Company", address="NNovgorod", mobile="9200150025", bday="4", bmonth="12", byear="1981"))
