import pytest
from pytest import fixture

import app
from src.config import FactoryConfigClass


def get_config_class(env):
    return FactoryConfigClass(env).config


@fixture(scope="session")
def get_api_client(env):
    run_env = get_config_class(env=env)
    app.app.config.update(run_env.__dict__)
    api = app.app.test_client()
    return api
