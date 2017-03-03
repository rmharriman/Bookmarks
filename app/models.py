from datetime import datetime
from flask import url_for
from . import db


class Tagging(db.Model):
    __tablename__ = "taggings"
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"), primary_key=True)
    bookmark_id = db.Column(db.Integer, db.ForeignKey("bookmarks.id"), primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


class Bookmark(db.Model):
    """SQLAlchemy provides a baseclass with a set of helper functions to inherit"""
    # Tablename is optional but convention uses plurals as table names so good practice to have
    __tablename__ = "bookmarks"
    # Remaining class vars are attributes of the model defined as instances of Columns
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(256), unique=True)
    title = db.Column(db.String(256), index=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    tags = db.relationship("Tagging",
                           foreign_keys=[Tagging.tag_id],
                           backref=db.backref("bookmark_tags", lazy="dynamic"),
                           lazy="dynamic",
                           cascade="all, delete-orphan"
                           )

    def to_json(self):
        json_bookmark = {
            "id": self.id,
            "url": self.url,
            "title": self.title
        }
        return json_bookmark

    @staticmethod
    def from_json(json_bookmark):
        bookmark = json_bookmark.get("bookmark")
        return Bookmark(url=bookmark.get("url"), title=bookmark.get("title"))


class Tag(db.Model):
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(256), unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_json(self):
        json_tag = {
            "id": self.id,
            "label": self.label,
            "timestamp": self.timestamp
        }
        return json_tag

    @staticmethod
    def from_json(json_tag):
        label = json_tag.get("label")
        return Tag(label=label)



