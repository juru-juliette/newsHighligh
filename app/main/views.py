from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_source,get_article


 # Views
@main.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    general = get_source('general')
    Business=get_source('business')
    Sports=get_source('sports')
    Entertainment=get_source('entertainment')
    Technology=get_source('technology')

    title='News Highlight Website'
    return render_template('index.html',title=title,general= general,business=Business,sports=Sports,entertainment=Entertainment,technology=Technology)

@main.route('/article/<id>')
def article(id):
    '''
    view root page function that returns the index page and its data
    '''
    article = get_article(id)
    print(get_article)
    title= "Top HeadLines Articles"
    return render_template('article.html',title=title, article = article )

