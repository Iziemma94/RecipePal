class Config:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///recipepal.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/mydatabase'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
