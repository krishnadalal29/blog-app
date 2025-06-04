from flask import Blueprint, render_template, flash, redirect, url_for
from .forms import LoginForm, RegisterForm
from .models import Post, User, load_user
from flask_login import logout_user, login_required, current_user, login_user

from . import db


main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template('index.html')

@main.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('main.user_posts'))
        flash('Invalid credentials')
    return render_template('login.html', form=form)


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('main.user_posts'))
    return render_template('registration.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/posts')
@login_required
def user_posts():
    posts = Post.query.filter_by(user_id=current_user.id).all()
    return render_template('user_posts.html', posts=posts)
