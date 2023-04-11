# -*- coding: utf-8 -*-
from model.project_model import Project

import random

def test_add_project(app, orm):
    project = Project(name="ANWw")
    old_projects = orm.get_project_list()
    app.project.create(project)
    new_projects = orm.get_project_list()
    # сравнение списков по содержанию, добавим такой же элемент в старый список
    old_projects.append(project)
    assert old_projects == new_projects
