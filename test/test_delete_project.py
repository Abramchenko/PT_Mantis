import random
from model.project_model import Project

def test_delete_project(app):
    username = app.config["webadmin"]["username"]
    password = app.config["webadmin"]["password"]
    if len(app.soap.get_project_list(username, password)) == 0:
        app.project.create(Project(name="test"))
    old_projects = app.soap.get_project_list(username, password)
    project = random.choice(old_projects)
    app.project.delete_project(project)
    new_projects = app.soap.get_project_list(username, password)
    # сравнение списков по содержанию, old - это список до удаления, поэтому удалим в нем выбранный элемент
    old_projects.remove(project)
    assert old_projects == new_projects