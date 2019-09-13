from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_source
from ..requests import get_article

 # Views
@main.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    general = get_source("general")
    

    title='News Highlight Website'
    return render_template('index.html',title=title,general= general)

@main.route('/article/<id>')
def article():
    '''
    view root page function that returns the index page and its data
    '''
    article=get_article(id)
    print(article)
    title= "Top HeadLines Articles"
    return render_template('article.html',title=title,article = article )

