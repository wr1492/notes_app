# notes_app

I focused on the login and security aspect of the project. I used Pycharm to edit my code.

I made a Flask web app for taking notes. I wanted to use all the parts that I've learned. 
The file structure is simple. The app.py only checks if the name and executes app.run():

from updated_notes import create_app

app = create_app()

if __name__ == '__main__':
    app.run()

I put the contents of the web app inside the updated_notes directory. I included an __init__.py. file,
so I could use it as a library. All the setup for the app is done within the 
__init__.py file. I created the function create_app() that is called when the app is run.

I used SQLAlchemy to create the database that is initiated in the __init__.py file. models.py file defines
the database. There are two tables in my database. Users that stores the users by a unique id and their
passwords. I used check_password_hash and generate_password_hash from werkzeug.security to secure the 
users passwords. The second table stores all the notes the user has created. By using sqlalchemy I was
able to insert notes into the database and retrieve them so the user could edit the note and update it then
save it back to the database. I used sessions to keep track of the logged-in users and their actions.

Inside the updated_notes directory is the static and templates directories; also, is the helper.py file that has 
a few funtions to do repetive task. The auth.py file houses all the routes for the web app. I set up a decoded 
function for the routes requiring login.

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function

Then I set up a decorated function to handle the catch @auth.after_request. Then the rest of the auth.py file
has 7 routes. most of the routs are getting the request from the form and updating the database with the info. 
