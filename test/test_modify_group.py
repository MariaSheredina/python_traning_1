# задание10
# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group(app):
    if app.group.count_group() == 0:
        app.group.create_group(Group(name="Old name", header="Old header", footer="Old header"))
    app.group.modify_first_group(Group(name="New name", header="New header", footer="New header"))
    app.session.logout()

def test_modify_group_name(app):
    if app.group.count_group() == 0:
        app.group.create_group(Group(name="Old name"))
    app.group.modify_first_group(Group(name="New name"))


def test_modify_group_header(app):
    if app.group.count_group() == 0:
        app.group.create_group(Group(header="Old header"))
    app.group.modify_first_group(Group(header="New header"))


def test_modify_group_footer(app):
    if app.group.count_group() == 0:
        app.group.create_group(Group(footer="Old footer"))
    app.group.modify_first_group(Group(footer="New footer"))
