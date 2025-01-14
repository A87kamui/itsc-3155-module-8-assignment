from flask import Flask, redirect, render_template, request
from src.repositories.movie_repository import movie_repository_singleton

app = Flask(__name__)

# This repository houses the scaffolding for a movie rating application. By the end, this application will cumplir the following user stories / features:

# As a user, I should be able to view all saved movie ratings in a visually appealing table
# As a user, I should be able to save a movie rating with the movie's name, directory, and a 1-5 rating
# As a user, I should be able to search for a specific movie rating using the movie's title

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    #creating a list of movies
    movie_directory = {}
    movieList = []
    movieList = movie_repository_singleton.get_all_movies()
    for movie in movieList:
        name = movie.title
        rating = movie.rating
        movie_directory[name] = rating
    return render_template('list_all_movies.html', list_movies_active=True, movies = movie_directory)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    #when user submits form, create a new movie
    title = request.form.get('title')
    director = request.form.get('director')
    rating = request.form.get('rating')
    movie_repository_singleton.create_movie(title, director, rating)
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    temp = []
    movie_name = request.args.get("title")
    temp = movie_repository_singleton.get_movie_by_title(movie_name)
    notFound = " "
    # if movie is found, set sentence to show movie
    if temp != None:
        title = temp.title
        director = temp.director
        rating = temp.rating
        sentence = "The movie " + title + " with director " + director + " has a rating of " + rating + "."   
    # if a movie cannot be found    
    if temp == None and movie_name != None:
        notFound = "Movie not found"
        sentence = " "
    # Nothing appears before movie is entered
    if movie_name == None:
        sentence = " "
    return render_template('search_movies.html', search_active=True, sentence = sentence, notFound = notFound) 

# run the application
if __name__ == "__main__":
   app.run(debug=True)
