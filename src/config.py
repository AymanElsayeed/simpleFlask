"""

Configuration module for the Flask API

"""


class FConfig(object):
    def __init__(self):
        pass


class ProductionConfig(FConfig):
    """
    Production configuration class
    """
    def __init__(self):
        super().__init__()
        self.FLASK_EXT_PORT = "30333"
        self.DEBUG = False
        self.LOGGING_PATH = "/synthetic/logs"


class DevelopmentConfig(FConfig):
    """
    Development configuration class
    """
    def __init__(self):
        super().__init__()
        self.FLASK_EXT_PORT = "30331"
        self.DEBUG = True
        self.LOGGING_PATH = "/synthetic/logs"


class TestingConfig(FConfig):
    """
    Testing configuration class
    """
    def __init__(self):
        super().__init__()
        self.TESTING = True
        self.FLASK_EXT_PORT = "30331"
        self.LOGGING_PATH = "/logs/flaskapi/testing/"
        self.NAMESPACE = "synthetic-process-testing"


class LocalConfig(FConfig):
    """
    Local configuration class
    """
    def __init__(self):
        super().__init__()
        self.TESTING = False
        self.ENV = "local"
        self.threaded = True
        self.debug = True
        self.ssv = "/Users/ayman/syndata"
        self.ssd = "/synthetic"
        self.LOGGING_PATH = "~/data/logs"
        self.logging_path = "~/syndata/logs"
        self.moc_data_path = "./data/MOCK_DATA.csv"
        self.regex_db = "./Src/regex_db.csv"
        self.data_path = "~/syndata/"
        self.DEFAULT_MAIN_DIR_FILE = self.data_path
        self.kube_files = "~/Documents/WProject/r-to-py-synthetic/API/Kubernetes/"


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
            self.config = FConfig()
