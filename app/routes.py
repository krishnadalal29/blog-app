from flask import Blueprint, render_template
from .models import Post
import os

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("frame_wrapper.html", page="base")

@main.route("/templates/<filename>")
def templates(filename):
    print("filename", filename)
    template_path = f"{filename}.html"
    if os.path.exists(os.path.join("app/templates/", template_path)):
        if filename == "index":
            posts = Post.query.all()
            return render_template("frame_wrapper.html", page=filename, posts=posts)
        else:
            return render_template("frame_wrapper.html", page=filename)
    else:
        return f"Page '{filename}' not found.", 404