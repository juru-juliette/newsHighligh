from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_source

 # Views
@main.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    general = get_source("general")
    

    title='News Highlight Website'
    return render_template('index.html',title=title,general= general)
