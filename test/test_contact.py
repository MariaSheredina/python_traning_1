# push_задание6
# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(
        Contact(firstname="Maria", middlename="Victorovna", lastname="Sidorova", nickname="Mari", company="Company",
                address="NNovgorod", mobile="9200150025", bday="4", bmonth="12", byear="1981"))
    app.session.logout()
