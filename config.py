import os

class Config:

    SOURCE_API_BASE_URL = 'https://newsapi.org/v2/sources?category={}&apiKey={}'
    SOURCE_API_KEY = '40bc02c9e4ec46e1ae7c5579b9bd433f'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    ARTICLE_API_BASE_URL = 'https://newsapi.org/v2/everything?id={}&apiKey={}'
    
  


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}