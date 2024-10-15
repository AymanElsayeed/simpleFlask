"""

Configuration module for the Flask API

"""
import os


class ABCConfig(object):
    def __init__(self):
        self.Logging_level = "INFO"
        self._LOGGING_PATH = "./logs/app/"
        self.logging_format = "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"

    @property
    def LOGGING_PATH(self):
        # check if the logging path is existing, if not create it
        if not os.path.exists(self._LOGGING_PATH):
            os.makedirs(self._LOGGING_PATH)
        return self._LOGGING_PATH

    @LOGGING_PATH.setter
    def LOGGING_PATH(self, value):
        self._LOGGING_PATH = value


class ProductionConfig(ABCConfig):
    """
    Production configuration class
    """

    def __init__(self):
        super().__init__()
        self.FLASK_EXT_PORT = "30333"
        self.DEBUG = False
        self.LOGGING_PATH = "./logs/app/production/"


class DevelopmentConfig(ABCConfig):
    """
    Development configuration class
    """

    def __init__(self):
        super().__init__()
        self.FLASK_EXT_PORT = "30331"
        self.DEBUG = True
        self.LOGGING_PATH = "./logs/app/development/"


class TestingConfig(ABCConfig):
    """
    Testing configuration class
    """

    def __init__(self):
        super().__init__()
        self.TESTING = True
        self.FLASK_EXT_PORT = "30331"
        self.LOGGING_PATH = "./logs/app/testing/"


class LocalConfig(ABCConfig):
    """
    Local configuration class
    """

    def __init__(self):
        super().__init__()
        self.TESTING = True
        self.ENV = "local"
        self.threaded = True
        self.FLASK_EXT_PORT = 30333
        self.HOST = "0.0.0.0"
        self.DEBUG = True
        self.LOGGING_PATH = "./logs/app/local/"
        self.Logging_level = "DEBUG"


class FactoryConfigClass:
    """
    Factory class to create the configuration class based on the environment
    """

    def __init__(self, env):
        print("the env is ", env)
        if env == "local":
            self.config = LocalConfig()
        elif env == "dev":
            self.config = DevelopmentConfig()
        elif env == "qa":
            print("the env is ", env)
            self.config = TestingConfig()
        elif env == "prod":
            self.config = ProductionConfig()
        else:
            self.config = ABCConfig()
