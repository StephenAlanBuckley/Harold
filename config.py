class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
#/Config

class ProductionConfig(Config):
    DEBUG = False
#/ProductionConfig

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
#/StagingConfig

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
#/DevelopmentConfig
