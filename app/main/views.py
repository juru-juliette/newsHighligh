# from flask import render_template
# from main import app
from flask import render_template,request,redirect,url_for
from . import main
# from ..requests import get_movies,get_movie,search_movie
# from .forms import ReviewForm
from ..models import Review
from .requests import get_source
 # Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    General_category=get_source("general")
    Business_category=get_source("business")
    Sports_category=get_source("sports")
    Entertainment_category=get_source("entertainment")
    Technology_category=get_source("technology")

    title='News Highlight Website'
    return render_template('index.html',title=title,general=General_cat,business=Business_cat,sports=Sports_cat,entertainment=Entertainment_cat,technology=Technology_cat)
