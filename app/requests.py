
# from app import main
import urllib.request,json
from .models import Source
from .article import Article
# Getting api key
api_key = None
# Getting the news base url
base_url =  None
article_url = None
def configure_request(app):
    global api_key, base_url,article_url
    api_key=app.config['SOURCE_API_KEY']
    print(api_key)
    base_url=app.config['SOURCE_API_BASE_URL']
    article_url=app.config['ARTICLE_API_BASE_URL']
    print(article_url)
def get_source(category):
    '''
    Function that gets the json response to url request
    '''
    get_source_url=base_url.format(category,api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data=url.read()
        get_source_response=json.loads(get_source_data)

        source_results= None

        if get_source_response ['sources']:
            source_results_list= get_source_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    '''            
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results=[]
    for source in source_list:
        id=source.get('id')
        name=source.get('name')
        description=source.get('description')
        url = source.get('url')

        if  id:
            source_object = Source(id,name,description,url)
            source_results.append(source_object)  

    return source_results    

def get_article(id):
    '''
    function that gets json request to the url
    '''
    get_article_url = article_url.format(id,api_key)
    print(get_article_url)

    with urllib.request.urlopen(get_article_url)as url:
        get_article_data=url.read()
        get_article_response=json.loads(get_article_data)

        article_results= None

        if get_article_response['articles']:
            article_results_list = get_article_response['articles']
            article_results = receive_result(article_results_list)

    return article_results        

def receive_result(article_list):
    '''
    Function  that processes the article result and transform them to a list of Objects

    Args:
    article_list: A list of dictionaries that contain article details

    Returns :
    article_results: A list of article objects
    '''

    article_results=[]
    for article in article_list:
        id=article.get('id')
        author=article.get('author')
        title=article.get('title')
        description=article.get('description')
        url=article.get('url')
        urlToImage=article.get('urlToImage')
        publishedAt=article.get('publishedAt')
        content=article.get('content')
        
        if author:
            article_object = Article(id,author,title,description,url,urlToImage,publishedAt,content)
            article_results.append(article_object)  

    return article_results 



