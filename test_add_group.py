# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture = Application
    request.addfinalizer(fixture.dectroy)
    return fixture

def test_add_group(app):
    wd = self.wd
    self.app.login(username="admin", password="secret")
    self.app.create_group(Group(name="fff", header="ttt", footer="hhh"))
    self.app.logout()

def test_add_empty_group(app):
    wd = self.wd
    self.app.login(username="admin", password="secret")
    self.app.create_group(Group(name="fff", header="ttt", footer="hhh"))
    self.app.logout()

