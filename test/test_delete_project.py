import random
from model.project_model import Project

def test_delete_project(app, orm):
    if len(orm.get_project_list()) == 0:
        app.project.create(Project(name="test"))
    old_projects = orm.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project(project)
    new_projects = orm.get_project_list()
    # сравнение списков по содержанию, old - это список до удаления, поэтому удалим в нем выбранный элемент
    old_projects.remove(project)
    assert old_projects == new_projects