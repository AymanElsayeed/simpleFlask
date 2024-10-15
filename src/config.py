"""

Configuration module for the Flask API

"""


class ABCConfig(object):
    def __init__(self):
        pass


class ProductionConfig(ABCConfig):
    """
    Production configuration class
    """
    def __init__(self):
        super().__init__()
        self.FLASK_EXT_PORT = "30333"
        self.DEBUG = False
        self.LOGGING_PATH = "./logs"


class DevelopmentConfig(ABCConfig):
    """
    Development configuration class
    """
    def __init__(self):
        super().__init__()
        self.FLASK_EXT_PORT = "30331"
        self.DEBUG = True
        self.LOGGING_PATH = "./logs"


class TestingConfig(ABCConfig):
    """
    Testing configuration class
    """
    def __init__(self):
        super().__init__()
        self.TESTING = True
        self.FLASK_EXT_PORT = "30331"
        self.LOGGING_PATH = "./logs/testing/"
        self.NAMESPACE = "process-testing"


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
        self.LOGGING_PATH = "./logs"


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
