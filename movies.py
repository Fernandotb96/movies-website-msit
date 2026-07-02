import movie_storage_sql as storage
import statistics
import random


def menu():
    """Print menu to user"""
    print("""
    ======= Fernando's Movies Database =======
    Menu:
     1. List of movies      2. Add movie
     3. Delete movie        4. Update rating
     5. Stats               6. Random movie
     7. Search movie        8. Movies sorted by rating
     9. Movies sorted by year 
     0. Exit program
    ===========================================""")


def list_of_movies():
    """Fetch the movies from database and print them in a list"""
    movies = storage.list_movies()
    if not check_movies_exist(movies):
        return
    print(f"There are {len(movies)} movies in total:")
    print("-" * 30)
    for movie, info in movies.items():
        print(f"'{movie}' from {info["year"]} with a rating of {info["rating"]}")
    print("-" * 30)


def number_input(prompt, error_prompt, is_float=False):
    """Ask user for a number with the given prompts and condition"""
    while True:
        try:
            user_input = input(prompt)
            if is_float:
                return float(user_input)
            return int(user_input)
        except ValueError:
            print(error_prompt)


def title_input(prompt):
    """Ask user for a movie name, ensuring it is not empty or just spaces."""
    while True:
        title = input(prompt).strip().title()
        if title:
            return title
        print("Error! The movie name cannot be empty. Please try again.\n")


def check_movies_exist(movies_dict):
    """Check if the database has movies. Prints an error if empty."""
    if not movies_dict:
        print("Error! The database is currently empty.")
        return False
    return True


def add_new_movie():
    """Add a new movie to the database asking user for name, year and rating."""
    title = title_input("Introduce the name of the new movie: ")
    rating_movie = number_input(
        "Introduce the rating of the new movie: ",
        "Error! Please introduce a decimal number for the rating [0-10].",
        is_float=True
    )
    year_movie = number_input(
        "Introduce the year of the new movie: ",
        "Error! Please introduce a valid number for the year."
    )
    storage.add_movie(title, year_movie, rating_movie)


def delete_movies():
    """Ask user for a movie to delete from the database"""
    title = title_input("Introduce the name of the movie to delete: ")
    storage.delete_movie(title)


def update_rating():
    """Ask for movie name and rating to update in the database"""
    title = title_input("Introduce the name of the movie to update: ")
    new_rating = number_input(
        "Introduce the new rating for the movie: ",
        "Error! Please introduce a decimal number for the rating [0-10].",
        is_float=True
    )
    storage.update_movie(title, new_rating)


def movies_stats():
    """Print statistics about the movies database (avg, median, max and min)."""
    movies = storage.list_movies()
    if not check_movies_exist(movies):
        return
    print("Movies stats: ")
    print("-" * 30)
    ratings = [info["rating"] for info in movies.values()]
    average_rating = statistics.mean(ratings)
    median_rating = statistics.median(ratings)
    print(f"-The average rating is {average_rating:.2f}")
    print(f"-The median rating is {median_rating:.2f}")
    # Best movie/es:
    max_rating = max(ratings)
    best_movies = [movie for movie, info in movies.items() if info["rating"] == max_rating]
    if len(best_movies) == 1:
        print(f"The best movie is '{best_movies[0]}' with a rating of {max_rating}")
    else:
        print(f"The best movies are: {best_movies} with a rating of {max_rating}")
    # Worst movie/es:
    min_rating = min(ratings)
    worst_movies = [movie for movie, info in movies.items() if info["rating"] == min_rating]
    if len(worst_movies) == 1:
        print(f"The worst movie is '{worst_movies[0]}' with a rating of {min_rating}")
    else:
        print(f"The worst movies are: {worst_movies} with a rating of {min_rating}")


def random_movie():
    """Print random movie with info"""
    movies = storage.list_movies()
    if not check_movies_exist(movies):
        return
    movie_name_list = list(movies.keys())
    random_choice = random.choice(movie_name_list)
    rating = movies[random_choice]["rating"]
    year = movies[random_choice]["year"]
    print(f"We recommend you the movie '{random_choice}' from {year} with rating of {rating}")


def movie_searcher():
    """Ask for title and search for a movie in the database"""
    movies = storage.list_movies()
    if not check_movies_exist(movies):
        return
    movie_search = input("Introduce the name of the movie you want to search: ").strip().lower()
    found_something = False
    print(f"-Search Results:")
    print("-" * 30)
    for movie, info in movies.items():
        if movie_search in movie.lower():
            found_something = True
            print(f"{movie}: From {info["year"]} with a rating of {info["rating"]}.")
    if not found_something:
        print(f"Error! Movie not found.")


def movies_by_rating():
    """Print movies sorted by rating in descending order"""
    movies = storage.list_movies()
    if not check_movies_exist(movies):
        return
    print(f"Movies sorted by rating:")
    print("-" * 30)
    movies_sorted = sorted(movies.items(), key=lambda x: x[1]["rating"], reverse=True)
    for movie, info in movies_sorted:
        print(f"'{movie}' [{info["year"]}]: {info["rating"]}")


def movies_by_year():
    """Print movies sorted by year in defined order(Normal or Reverse)"""
    movies = storage.list_movies()
    if not check_movies_exist(movies):
        return
    decision = input("Do you want to sort by year incrementally? (y/n): ").strip().lower()
    descending = decision not in ("y", "yes")
    print(f"Movies sorted by year:")
    print("-" * 30)
    movies_sorted_year = sorted(movies.items(), key=lambda x: x[1]["year"], reverse=descending)
    for movie, info in movies_sorted_year:
        print(f"'{movie}' [{info["year"]}]: {info["rating"]}")


def main():
    """
    Orchestrate the main application flow.

    Initialize the database, then enter the main loop to display the
    menu and execute user-selected operations based on the router dictionary.
    """
    storage.init_database()
    router = {
        "1": list_of_movies,
        "2": add_new_movie,
        "3": delete_movies,
        "4": update_rating,
        "5": movies_stats,
        "6": random_movie,
        "7": movie_searcher,
        "8": movies_by_rating,
        "9": movies_by_year
    }
    while True:
        menu()
        user_decision = input(f"\nEnter a choice [0-9]: ").strip()
        if user_decision == "0":
            print(f"Thanks for the visit, have a nice day!")
            break
        elif user_decision in router:
            command = router[user_decision]
            command()
            input("\nPress Enter to continue...")
        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()
