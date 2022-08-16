#push_задание6
# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create_group(Group(name="fff", header="ttt", footer="hhh"))
    app.session.logout()

