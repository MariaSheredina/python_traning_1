# push_задание7
# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create_group(Group(name="name_Old", header="header_Old", footer="footer_Old"))

def test_add_group_empty(app):
    app.group.create_group(Group(name="", header="", footer=""))

