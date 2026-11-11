# GameShelf

GameShelf is a web application developed with Django that allows users to manage video games, genres, gaming platforms, and reviews.

The project was created as part of the SoftUni Python Web — Django Basics course.

## Features

- Create, view, edit, and delete games.
- Manage game genres and gaming platforms.
- Create and manage game reviews.
- Rate games on a scale from 1 to 100.
- Display reviews associated with each game.
- Filter games by genre and platform.
- Sort games by title or release date.
- Upload game images.
- Custom form validation and error messages.
- Custom template filter for rating labels.
- Custom 404 error page.
- Responsive interface using Bootstrap.

## Technologies

- Python 3.11
- Django 5.2
- SQLite
- HTML and CSS
- Bootstrap 5
- Pillow

## Project Structure

```text
GameShelf/
├── games/
├── platforms/
├── reviews/
├── gameshelf/
├── templates/
├── static/
├── manage.py
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/DzhmS/GameShelf.git
cd GameShelf
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open the application at:

http://127.0.0.1:8000/

The project starts with an empty database. Genres and platforms can be created through the interface before adding games and reviews.

## Main Pages

| Page | URL |
|---|---|
| Home / Games | `/` |
| Games | `/games/` |
| Genres | `/games/genres/` |
| Platforms | `/platforms/` |
| Reviews | `/reviews/` |
| Add Game | `/games/create/` |
| Add Genre | `/games/genres/create/` |
| Add Platform | `/platforms/create/` |
| Add Review | `/reviews/create/` |

## Validation

The application uses customized Django ModelForms with field validation.

- Game titles must contain at least two characters.
- Genre and platform names must contain at least two characters and be unique.
- Review ratings must be between 1 and 100.
- Review comments are optional, but non-empty comments must contain at least five characters.
- A review's associated game cannot be changed during editing.

## Custom Template Filter

The `score_label` filter converts numerical ratings into descriptive labels:

| Score | Label |
|---|---|
| 90–100 | Excellent |
| 75–89 | Very Good |
| 60–74 | Good |
| 40–59 | Average |
| 1–39 | Poor |

## Notes

This project is intended for educational purposes. SQLite is used as the development database. Uploaded media and local database files are not included in the repository.