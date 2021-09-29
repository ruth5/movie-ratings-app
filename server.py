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
    """Show all users in the datbase."""
    all_users = crud.return_all_users()

    return render_template('all_users.html', all_users=all_users)

@app.route('/users/<user_id>')
def show_user(user_id):
    """Show details on a particular user."""

    user_details = crud.get_user_by_id(user_id)

    return render_template('user_details.html', user = user_details)

@app.route('/users', methods = ['POST'])
def retrieve_login_data():
    """Register a user with a email and password."""
    email = request.form.get('email')
    password = request.form.get('password')

    print(20 * '*')
    print(f'user is {crud.get_user_by_email("user0@test.com")}')
    print(20 * '*')

    if crud.get_user_by_email(email):
        flash("Your account already exists.")
    else:
        crud.create_user(email, password)
        flash("Thanks for making an account.")
    
    return redirect("/")

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
