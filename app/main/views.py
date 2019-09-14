from flask import render_template ,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles
from ..models import Sources

#views
@main.route('/')
def index():
    '''
    view root page function thta returns the page and its data
    '''
    sources = get_sources('business')
    sports_sources = get_sources('sports')
    technology_sources = get_sources('entertainment')
    title = "News Highlights"


    return render_templates('index.html',title = title, sources = sources, sports_sources = sports_sources, technology_sources = technology_sources, entertainment_sources = entertainment_sources)

@app.route('/sources/<id>') 
def articles(id):
    '''
    view articles
    '''
    articles = get_articles(id)
    title = f'NH | {id}'

    return render_template('articles.html',title = title, articles = articles)   
   