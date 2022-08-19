# урок3_3
# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group(app):
    if app.group.count_group() == 0:
        app.contact.create_group(Group(name="Old group", header="Old_header", footer="Old_header"))
    app.contact.modify_first_group(Group(name="New group", header="New_header", footer="New_header"))


def test_modify_group_name(app):
    if app.group.count_group() == 0:
        app.contact.create_group(Group(name="Old group"))
    app.contact.modify_first_group(Group(name="New group"))


def test_modify_group_header(app):
    if app.group.count_group() == 0:
        app.contact.create_group(Group(name="Old header"))
    app.contact.modify_first_group(Group(name="New header"))


def test_modify_group_footer(app):
    if app.group.count_group() == 0:
        app.contact.create_group(Group(name="Old footer"))
    app.contact.modify_first_group(Group(name="New footer"))
