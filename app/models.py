from flask import url_for
from . import db


class Bookmark(db.Model):
    """SQLAlchemy provides a baseclass with a set of helper functions to inherit"""
    # Tablename is optional but convention uses plurals as table names so good practice to have
    __tablename__ = "bookmarks"
    # Remaining class vars are attributes of the model defined as instances of Columns
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(256), unique=True)
    title = db.Column(db.String(256), index=True)

    def to_json(self):
        json_bookmark = {
            "id": self.id,
            "url": self.url,
            "title": self.title
        }
        return json_bookmark
