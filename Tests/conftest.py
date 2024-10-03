"""

This module contains the fixtures that are used to run the tests.

"""

from pytest import fixture
from flaskProject.src.config import FactoryConfigClass
from flaskProject import app


def pytest_addoption(parser):
    parser.addoption("--env", action="store", help="environment to ru tests against")


@fixture(scope="session")
def env(request):
    """
    get the environment to run the tests against.
    :param request: the request object
    :return: the environment to run the tests against
    """
    env = request.config.getoption("--env")
    return env


def get_config_class(env):
    """
    get the config class based on the environment.
    :param env:  the environment to run the tests against
    :return: the config class
    """
    return FactoryConfigClass(env).config


@fixture(scope="session")
def client(env):
    """
    create a test client to run tests against.
    :param env: the environment to run the tests against
    :return: an instance of the test client
    """
    run_env = get_config_class(env=env)
    app.app.config.update(run_env.__dict__)
    api = app.app.test_client()
    return api
