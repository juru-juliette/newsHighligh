import os

class Config:

    NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?apiKey=40bc02c9e4ec46e1ae7c5579b9bd433f'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}