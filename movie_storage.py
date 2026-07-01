import json


def get_movies():
    """Loads the information from the JSON file and returns the data"""
    try:
        with open("movies_database.json", "r") as movie_file:
            movies_data = json.load(movie_file)
            return movies_data
    except FileNotFoundError:
        print("Error! File wasn't found")
        save_movies({})
        return {}


def save_movies(movies):
    """
  Gets all your movies as an argument and saves them to the JSON file.
  """
    try:
        json_data = json.dumps(movies)
        with open("movies_database.json", "w") as movie_file:
            movie_file.write(json_data)
    except OSError:
        print("Error! Could not write the file due to a system issue.")


def add_movie(title, year, rating):
    """Loads the data from the JSON file, adds a new movie to the dict and saves it."""
    movies = get_movies()
    if title not in movies:
        movies[title] = {"Rating": rating, "Year": year}
        save_movies(movies)
        print(f"The movie '{title}' was added to the list!")
    else:
        print(f"Error! The movie is already in the list!")


def delete_movie(title):
    """Loads movies from JSON file, deletes the movie and saves it."""
    movies = get_movies()
    if not movies:
        print("Error! The database is currently empty.")
        return
    if title in movies:
        del movies[title]
        print(f"The movie '{title}' was deleted")
        save_movies(movies)
    else:
        print(f"Error! '{title}' was not found")


def update_movie(title, rating):
    """Loads movies from JSON file, updates the movie with new rating and saves it."""
    movies = get_movies()
    if not movies:
        print("Error! The database is currently empty.")
        return
    if title in movies:
        movies[title]["Rating"] = rating
        save_movies(movies)
        print(f"Now '{title}' has a rating of {rating}")
    else:
        print(f"Error! '{title}' is not in the list.")
