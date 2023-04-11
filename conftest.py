from fixture.application import Application
from fixture.orm import ORMFixture
import pytest
import json
import os.path


fixture = None
target = None
def  load_config(file):
    global target
    if target is None:   # чтобы открыть его и считать однажды вначале
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target

@pytest.fixture (scope="session")
def orm():
    ormfixture = ORMFixture(host="127.0.0.1", name="bugtracker", user="root", password="")
    return ormfixture

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))["web"]
    web_admin = load_config(request.config.getoption("--target"))["webadmin"]
    if fixture is None or not fixture.is_valid(): # если что, перезапустить фикстуру
        fixture = Application(browser=browser, base_url= web_config["base_url"])
    fixture.session.login(username=web_admin["username"], password=web_admin["password"])
    return fixture

# такая фикстура выполняется один раз, в конце

@pytest.fixture(scope="session", autouse=True) # нигде не используется
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")





