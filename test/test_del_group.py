# задание10
# -*- coding: utf-8 -*-
from model.group import Group


def test_del_group(app):
    if app.group.count_group() == 0:
        app.group.create_group(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.del_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)

