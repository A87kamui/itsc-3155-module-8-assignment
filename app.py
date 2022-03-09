from flask import Flask, redirect, render_template
from src.repositories.movie_repository import movie_repository_singleton

app = Flask(__name__)

movie_list = [] #creates a empty list 
movie_dictionary = {} #creates an empty directory 


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    movie_list = movie_repository_singleton.get_all_movies() #store list of all movies in movie_list
    for movie in movie_list: #iterate through movie_list and store each element into movie
        name = movie.title  #store movie title in name
        rating = movie.rating   #store movie rating in rating
        movie_dictionary[name] = rating #use name as key and rating as value to store in movie_dictionary
    # TODO: Feature 1
    return render_template('list_all_movies.html', list_movies_active=True, movie_dictionary = movie_dictionary)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)
