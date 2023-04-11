from pony.orm import *
from model.project_model import Project


class ORMFixture:
    db=Database()
    class ORMProject(db.Entity):
        _table_ = "mantis_project_table"
        id = PrimaryKey(int, column="id")
        name = Optional(str, column="name")
        status = Optional(int, column="status")
        enabled = Optional(	int, column="enabled")
        view_state = Optional(int, column="view_state")
        description = Optional(str, column="description")


    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.db.bind("mysql", host=host, database=name, user=user, password=password)
        # сопоставление свойств классов и полей таблиц
        self.db.generate_mapping()

    def convert_projects_to_model(self, projects):
        def convert(project):
            return Project( id=str(project.id), name=project.name)
        return list(map(convert, projects))


    @db_session
    def get_project_list(self):
        # запрос на ЯП , sql будет сгенерирован автоматически. Данные выбираются и преобразуются в классы
        return self.convert_projects_to_model(list(select(p for p in ORMFixture.ORMProject)))

