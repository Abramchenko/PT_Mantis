
from selenium.webdriver.common.by import By

class ProjectHelper():
    def __init__(self, app):
        self.app = app

    project_cache = None

    def open_manage_page(self):
        wd = self.app.wd
        self.app.session.login("administrator", "root")
        wd.get ('http://localhost/mantisbt-1.2.20/my_view_page.php')
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_css_selector('input[type="submit"]').click()
        wd.find_element_by_link_text("Manage Projects").click()


    def create(self, project):
        wd = self.app.wd
        self.open_manage_page()
        wd.find_element_by_css_selector('input[value="Create New Project"]').click()
        self.fill_project_form(project)
        wd.find_element_by_css_selector('input[value="Add Project"]').click()
        self.project_cache = None


    def fill_project_form(self, project):
        self.change_field_value("name", project.name)
        self.change_field_value("status", project.status)
        self.change_field_value("enabled", project.enabled)
        self.change_field_value("view_state", project.view_state)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            if not(field_name in ("status","enabled", "view_state")):
                wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def select_project_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" %id).click()
    def delete_project(self, project):
        wd = self.app.wd
        #self.app.session.login("administrator", "root")
        self.open_manage_page()
        wd.find_element_by_link_text("%s" %project.name).click()
        wd.find_element(By.CSS_SELECTOR, "[value='Delete Project']" ).click()
        wd.find_element(By.CSS_SELECTOR, "[value='Delete Project']").click()
        self.group_cache = None



