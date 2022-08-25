# задание10
# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create_group(Group(name="name1", header="header1", footer="footer1"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


