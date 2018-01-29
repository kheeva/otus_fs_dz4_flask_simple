# Simple Flask app

You can create a simple web application using Flask, SQLAlchemy and patterns we used here. 


# How to Install

You just need to download and install python if you already haven't: http://python.org .

Install the modules:
```
pip install Jinja2
pip install Flask-Migrate
pip install flask_script
pip install flask-bootstrap

```

Clone this repo:
```
git clone https://github.com/kheeva/otus_fs_dz4_flask_simple
```

# How to use
Customize your settings in config.py

Customize your data models in manage.py.
Make your db:
```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

Customize your view funcs in `flask_app.py`.

Put your templates in templates/ dir.
Put your static file in static/ dir.

# Testing

```
python flask_app.py
```

Connect via broser to `http://127.0.0.1:5000/your_urls`

# Project Goals

The code is written for educational purposes. Training courses: otus.ru)
