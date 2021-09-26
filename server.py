"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# Replace this with routes and view functions!

@app.route('/')
def create_homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/movies')
def all_movies():
    """Show all movies in the database."""
    all_movies = crud.return_all_movies()

    return render_template('all_movies.html', all_movies=all_movies)

@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    "Show details on a particular movie."

    movie_details = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie = movie_details)

@app.route('/users')
def all_users():
    pass

@app.route('/users/<email>')
def show_user(email):
    pass


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
