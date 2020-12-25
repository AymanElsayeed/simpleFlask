from pytest import fixture
from flaskProject.src.config import FactoryConfigClass
from flaskProject import app


def pytest_addoption(parser):
    parser.addoption("--env", action="store", help="environment to ru tests against")


@fixture(scope="session")
def env(request):
    env = request.config.getoption("--env")
    return env


def get_config_class(env):
    return FactoryConfigClass(env).config


@fixture(scope="session")
def client(env):
    run_env = get_config_class(env=env)
    app.app.config.update(run_env.__dict__)
    api = app.app.test_client()
    return api
