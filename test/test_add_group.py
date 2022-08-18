# push_задание7
# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create_group(Group(name="Old", header="Old", footer="Old"))
    app.session.logout()



