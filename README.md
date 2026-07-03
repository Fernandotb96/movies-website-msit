# Movies Website MSIT

A Python project developed as part of the MSIT Software Development course.

The application allows users to build and manage a movie collection using data from the OMDb API, store it in a SQLite database, and generate a simple HTML website displaying all saved movies.

---
## Features

- Search movies using the OMDb API
- Store movies in a SQLite database
- List all saved movies
- Update movie ratings
- Delete movies
- Display movie statistics
- Search movies by title
- Sort movies by rating or release year
- Select a random movie
- Generate a static HTML website from the movie database

---

## Technologies

- Python
- SQLite
- SQLAlchemy
- OMDb API
- HTML
- CSS

---

## Installation


Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```text
API_KEY=your_omdb_api_key
```

You can obtain a free API key from:

https://www.omdbapi.com/apikey.aspx

---

## Usage

Run the application:

```bash
python movies.py
```

Follow the menu displayed in the terminal to manage your movie collection.

To generate the website, choose the corresponding menu option. 
An `index.html` file will be created automatically.

---