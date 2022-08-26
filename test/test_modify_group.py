# задание11
# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    if app.group.count_group() == 0:
        app.group.create_group(Group(name="Old name"))
    old_groups = app.group.get_group_list()
    group = Group(name="New name")
    group.id_g = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_header(app):
    if app.group.count_group() == 0:
        app.group.create_group(Group(header="Old header"))
    old_groups = app.group.get_group_list()
    group = Group(header="New header")
    group.id_g = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_footer(app):
    if app.group.count_group() == 0:
        app.group.create_group(Group(footer="Old footer"))
    old_groups = app.group.get_group_list()
    group = Group(footer="New footer")
    group.id_g = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
