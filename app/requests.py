# import urllib.request,json
# from .models import Movie
# # Getting api key
# api_key = None
# # Getting the movie base url
# base_url = None

# def configure_request(app):
#     global api_key,base_url
#     api_key = app.config['NEWS_API_KEY']
#     base_url = app.config['NEWS_API_BASE_URL']
from app import main
import urllib.request,json
from .models import News

Source=source.Source
# Getting api key
api_key=app.config['SOURCE_API_KEY']
# Getting the news base url
base_url=app.config['SOURCE_API_BASE_URL']