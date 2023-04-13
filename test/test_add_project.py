# -*- coding: utf-8 -*-
from model.project_model import Project
import string

import random
def random_name(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix+"".join(random.choice(symbols) for i in range (random.randrange(maxlen)))
def test_add_project(app):
    username = app.config["webadmin"]["username"]
    password = app.config["webadmin"]["password"]
    project = Project(name = random_name("Project_", 10))
    old_projects = app.soap.get_project_list(username, password)
    app.project.create(project)
    new_projects = app.soap.get_project_list(username, password)
    # сравнение списков по содержанию, добавим такой же элемент в старый список
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
