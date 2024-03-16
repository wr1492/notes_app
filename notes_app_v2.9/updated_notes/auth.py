from functools import wraps
from flask import Blueprint, render_template, request, redirect, session
from werkzeug.security import check_password_hash, generate_password_hash
from . import db
from .models import User, Note
from .helper import apology, wiki_search

auth = Blueprint('auth', __name__)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


@auth.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@auth.route('/')
def index():
    return render_template("index.html")


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if not email:
            return apology("Please enter a valid email", 400)
        elif len(password) < 6:
            return apology("password must be 6 characters", 400)
        elif not user:
            return apology("Email must match", 400)
        elif not check_password_hash(user.password, password):
            return apology("incorrect password", 400)
        else:
            # Remember which user has logged in
            session["user_id"] = user.id
            return redirect("/dashboard")

    return render_template("login.html")


@auth.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        user_name = request.form.get("user_name")
        email = request.form.get("email")
        password = request.form.get("password")
        password1 = request.form.get("password1")
        existing_user = db.session.query(User).filter_by(email=email).first()

        if existing_user:
            return apology("Already registered, please login", 400)
        elif not email:
            return apology("Please enter a valid email", 400)
        elif len(user_name) < 3:
            return apology("username must be 3 characters", 400)
        elif len(password) < 6:
            return apology("password must be 6 characters", 400)
        elif password != password1:
            return apology("Passwords must match", 400)
        else:
            new_user = User(email=email, password=generate_password_hash(password), user_name=user_name)
            db.session.add(new_user)
            db.session.commit()
            return redirect("/login")
    return render_template('register.html')


@auth.route("/logout")
def logout():
    """Log user out"""
    session.clear()

    # Redirect user home page
    return redirect("/")


@auth.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    user_id = session.get("user_id")
    if request.method == "POST":
        subject = request.form.get('subject')
        note = request.form.get("note")
        title = request.form.get("title")

        if len(note) < 1:
            return apology('Note is to short', 400)
        else:
            new_note = Note(title=title, data=note, user_id=user_id, subject=subject)
            db.session.add(new_note)
            db.session.commit()
    return render_template("dashboard.html")


@auth.route("/wiki_search", methods=["GET", "POST"])
@login_required
def wiki():
    user_id = session.get("user_id")
    if request.method == "POST":
        search = request.form.get('wiki_search')
        if len(search) < 1:
            return apology("Please enter search term", 400)
        else:
            return wiki_search(search)
    return render_template("wiki_search.html")


@auth.route("/notes", methods=["GET", "POST"])
@login_required
def notes():
    user_id = session.get("user_id")
    notes = Note.query.filter_by(user_id=user_id)
    """Show all notes"""
    return render_template("notes.html", notes=notes)


@auth.route("/edit", methods=["POST", "GET"])
@login_required
def edit():
    if request.method == "POST":
        note_id = request.form.get("note_id")
        note = Note.query.get(note_id)
        if note:
            # Render the edit.html template with the note data
            return render_template("edit.html", note=note)

    edited_note = request.form.get("edited_note")
    if edited_note:
        edit_note_id = request.form.get("edit_note_id")
        edit_note = Note.query.get(edit_note_id)
        edit_note.data = edited_note
        # Commit the changes to the database
        db.session.commit()
        return redirect("/notes")

    else:
        return "Invalid note ID"


@auth.route("/delete", methods=["GET", "POST"])
@login_required
def delete():
    if request.method == "POST":
        note_id = request.form.get("id")
        note = Note.query.get(note_id)
        db.session.delete(note)
        db.session.commit()
        return redirect("/notes")
