#push_задание5
# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.dectroy)
    return fixture


def test_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Maria", middlename="Victorovna", lastname="Sidorova", nickname="Mari", company="Company", address="NNovgorod", mobile="9200150025", bday="4", bmonth="12", byear="1981"))
    app.session.logout()
