#push_задание5
# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application
from fixture.session import SessionHelper
from fixture.group import GroupHelper

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.dectroy)
    return fixture

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="fff", header="ttt", footer="hhh"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

