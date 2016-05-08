import sqlite3
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash

#############################
###     Config
##
DATABASE = 'labrat.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'admin'



app = Flask(__name__)
app.config.from_object(__name__)
# app.config.from_envvar('LABRAT_SETTINGS', silent=True)




#############################
###     Routes
##
@app.route('/')
def home():
    return "hello world!"

@app.route('/login')
def welcome():
    return render_template

@app.route('/register')
def register():



#############################
###     Launcher
##
if __name__ == '__main__':
    app.run(debug=DEBUG)

#############################
###     Functions:
##
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


































    
