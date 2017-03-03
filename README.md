# Bookmarks

Basic API to serve as the backend for a js app

#### To start development environment:
1. pip install -r requirements.txt
2. Export development environment database URI
`export DEV_DATABASE_URI=sqlite:////tmp/dev.db`
3. Export flask app location 
`export FLASK_APP=bookmark_app.py`
4. Setup the database: flask db init, flask db migrate, flask db upgrade
5. Start server: flask run
