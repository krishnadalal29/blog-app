from flask import Blueprint, render_template
<<<<<<< HEAD
from .forms import LoginForm
from .models import Post, User
=======
from .models import Post
>>>>>>> 7da42ac921eab4ce1238c983788457f2a89a4871
import os

main = Blueprint("main", __name__)


@main.route("/")
def index():
    posts = Post.query.all()
    return render_template("frame_wrapper.html", page="base", posts=posts)

@main.route("/templates/<filename>")
def templates(filename):
    template_path = f"{filename}.html"
    if os.path.exists(os.path.join("app/templates/", template_path)):
        if filename == "index":
            posts = Post.query.all()
            return render_template("frame_wrapper.html", page=filename, posts=posts)
        elif filename == "login":
            form = LoginForm()
            return render_template("frame_wrapper.html", page=filename, form=form)
        elif filename == "register":
            return render_template("frame_wrapper.html", page=filename)
        else:
            return render_template("frame_wrapper.html", page=filename)
    else:
        return f"Page '{filename}' not found.", 404

@main.route("/login", methods=["POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            print("Login successful")
            return render_template("frame_wrapper.html",page="index", posts=Post.query.all())
        else:
            print("Login failed")
            form.username.errors.append("Invalid username or password")
            return render_template("frame_wrapper.html", page="login", form=form, error=form.errors)
    else:
        return render_template("frame_wrapper.html", page="login", form=form, error=form.errors)
