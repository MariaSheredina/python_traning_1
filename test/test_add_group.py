# push_задание7
# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create_group(Group(name="New1", header="New1", footer="New1"))
    app.session.logout()



