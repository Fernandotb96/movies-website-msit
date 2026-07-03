TEMPLATE_PATH = "templates/index_template.html"


def serialize_movie(title, info):
    """Transform the dict of the movie into a single HTML <li> element"""
    movie_block = f"""
                    <li>
                        <div class="movie">
                            <img class="movie-poster"
                                src="{info["poster"]}"/>
                            <div class="movie-title">{title}</div>
                            <div class="movie-year">{info["year"]}</div>
                        </div>
                    </li>"""
    return movie_block


def movies_to_html_list(movies):
    """Create an HTML list from the movies dict"""
    output = "".join([serialize_movie(title, info) for title, info in movies.items()])
    return output


def replace_template_text(html_text):
    """Replace the template text with new movies HTML list"""
    try:
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as file:
            old_text = file.read()
            new_text = old_text.replace("__TEMPLATE_MOVIE_GRID__", html_text)
            return new_text
    except Exception as e:
        print(f"Error replacing new movie's text: {e}")


def create_html(html_text):
    """Create an HTML file with an HTML text"""
    try:
        with open("index.html", "w", encoding="utf-8") as file:
            file.write(html_text)
            print("Website created successfully")
    except Exception as e:
        print(f"Error creating HTML file: {e}")


def create_website(movies):
    """Creates a website from the movies dict"""
    movies_text = movies_to_html_list(movies)
    final_text = replace_template_text(movies_text)
    create_html(final_text)
