from suds.client import Client
from suds import WebFault
from model.project_model import Project

class SoapHelper:
    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.me_login(username, password)
            return True
        except WebFault:
            return False
    def convert_projects_to_model(self, projects):
        def convert(project):
            return Project(id=project.id, name=project.name)
        return list(map(convert, projects))

    def get_project_list(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        projects = self.convert_projects_to_model(list(client.service.mc_projects_get_user_accessible(username, password)))
        return projects