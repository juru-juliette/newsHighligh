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
    def get_source(category):
    '''
    Function that gets the json response to url request
    '''
    get_source_url=base_url.format(category,api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data=url.read()
        get_source_response=json.loads(get_source_data)

        source_results= None


        # if get_source_response ['sources']:
        #     source_results_list=get_source_response['sources']

        if get_source_response ['sources']:
            source_results_list=get_source_response['sources']
            source_results= process_results(source_results_list)

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

        if  id:
            source_Object = Source(id,name,description)
            source_results.append(source_Object)  

    return source_results    

    