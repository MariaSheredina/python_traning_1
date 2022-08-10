# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application
from fixture.session import SessionHelper

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.dectroy)
    return fixture

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="fff", header="ttt", footer="hhh"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()

