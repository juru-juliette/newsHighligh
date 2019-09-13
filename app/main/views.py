# from flask import render_template
# from main import app
from flask import render_template,request,redirect,url_for
from . import main
# from ..requests import get_movies,get_movie,search_movie
# from .forms import ReviewForm
from ..models import Review
 # Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')