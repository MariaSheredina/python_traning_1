# задание10
# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group(app):
    if app.group.count_group() == 0:
        app.group.create_group(Group(name="Old name", header="Old header", footer="Old header"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="New name", header="New header", footer="New header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_name(app):
    if app.group.count_group() == 0:
        app.group.create_group(Group(name="Old name"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="New name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    if app.group.count_group() == 0:
        app.group.create_group(Group(header="Old header"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="New header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_footer(app):
    if app.group.count_group() == 0:
        app.group.create_group(Group(footer="Old footer"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(footer="New footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
