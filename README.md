This is the first Flask app. I used Pycharm to edit my code.

I made a Flask web app for taking notes. I wanted to have some research tools. I added a wikipidia search. 
I am working on adding a tools sidebar that will have a calculator, to-do-list and a few others.
The file structure is simple. The app.py only checks if the name and executes app.run():

from website import create_app

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
save it back to the database. The user can search the notes by subject. I used sessions to keep track of the logged-in users and their actions.

Inside the updated_notes directory is the static and templates directories; along with the auth.py file.
The auth.py file houses all the routes for the web app. I set up a decoded function for the routes
requiring login.

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function

Then I set up a decorated function to handle the catch @auth.after_request. Then the rest of the auth.py file
has 10 routes. most of the routs are getting the request from the form and updating the database with the info. 
The most complicated route for me was the /edit route. I had to get the note id and send it to the route inside 
a form that the template could send back after editing. The user could update the note and save it to the 
database.

I did the css and style from scratch vs using a bootstrap. The style is basic and is in the static directory. I cleaned up 
the css from the first version, I had 4 style sheets linked to the layout. There are now only two. 
