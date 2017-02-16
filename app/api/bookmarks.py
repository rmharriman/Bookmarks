from flask import jsonify, request, url_for
from . import api
from app import db
from app.models import Bookmark


@api.route("/bookmarks/")
def get_bookmarks():
    bookmarks = Bookmark.query.all()
    return jsonify({"bookmarks": [bookmark.to_json() for bookmark in bookmarks]})


@api.route("/bookmarks/<int:id>")
def get_bookmark(id):
    bookmark = Bookmark.query.get_or_404(id)
    return jsonify(bookmark.to_json())


@api.route("/bookmarks/", methods=["POST"])
def new_post():
    bookmark = Bookmark.from_json(request.json)
    db.session.add(bookmark)
    db.session.commit()
    return jsonify(bookmark.to_json()), 201, \
        {"Location": url_for("api.get_bookmark", id=bookmark.id, _external=True)}


@api.route("/bookmarks/<int:id>", methods=["PUT"])
def edit_bookmark(id):
    bookmark = Bookmark.query.get_or_404(id)
    bookmark.title = request.json.get("title", bookmark.title)
    db.session.add(bookmark)
    return jsonify(bookmark.to_json())


@api.route("/bookmarks/<int:id>", methods=["DELETE"])
def delete_bookmark(id):
    bookmark = Bookmark.query.get_or_404(id)
    bookmark.title = request.json.get("title", bookmark.title)
    db.session.delete(bookmark)
    return {"result": True}
