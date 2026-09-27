# TaskMaster-Flask-Python

A small Flask learning project that builds from a basic route and static page into a database-backed task manager.

## Features

- Basic Flask route returning a text response.
- HTML pages rendered with Flask and Jinja templates.
- Shared base templates and static CSS styling.
- Task manager using Flask-SQLAlchemy and SQLite, with add, list, update, and delete operations.

## Project structure

```text
.
├── appintrobasics1.py        # Basic Flask app
├── app_rendertemplate2.py    # Render a template
├── app_dynamic3.py           # Template inheritance example
├── app_static4.py            # Template with static CSS
├── app_db5.py                # SQLite-backed task manager
├── requirements.txt
├── static/css/main.css
└── templates/                # Jinja templates
```

## Requirements

- Python 3.10 or newer
- pip

## Setup

From the project directory, create and activate a virtual environment, then install the dependencies:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

On Windows, activate the environment with `.venv\Scripts\activate` instead.

## Run

Run any example from the project directory. For example, to start the task manager:

```sh
python app_db5.py
```

Open <http://127.0.0.1:5000/> in a browser. Other examples can be started by replacing `app_db5.py` with `appintrobasics1.py`, `app_rendertemplate2.py`, `app_dynamic3.py`, or `app_static4.py`.

## Database initialization

The task manager stores its SQLite database at `instance/site.db`. Create the database tables once before the first run:

```sh
python -c 'from app_db5 import app, db; app.app_context().push(); db.create_all()'
```

This uses the application context required by Flask-SQLAlchemy. The `instance/` directory and database are generated locally and excluded from Git.

## Notes

- `app_db5.py` defines a `User` model for task records and exposes the task create, update, and delete routes.
- The app scripts use Flask's development server with debug mode enabled. Use debug mode only for local development, not production.
