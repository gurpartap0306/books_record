import os

from flask import Flask, session,render_template,request
from flask_session import Session
from sqlalchemy import create_engine,exc
from sqlalchemy.orm import scoped_session, sessionmaker
import requests

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/registred",methods=["POST"])
def registred():
    username=request.form.get("username")
    password=request.form.get("password")
    try:
        db.execute("INSERT INTO users (username , password) VALUES (:username ,:password)",{"username": username,"password": password})
    except exc.IntegrityError:
        return render_template("error.html",message="user already exixts.")
    db.commit()
    return render_template("index.html")

@app.route("/home",methods=["GET","POST"])
def home():
    if request.method == "GET":
        return "please login to access this page"
    else:
        username=request.form.get("username")
        password=request.form.get("password")
        if db.execute("SELECT * FROM users WHERE username=:username AND password=:password",{"username": username,"password": password}).rowcount==1:
            return render_template("home.html")
        else:
            return render_template("error.html",message="username or password is incorrect")
        db.commit()

@app.route("/home2")
def home2():
    return render_template("home.html")

@app.route("/search", methods=["POST"])
def search():
    isbn = request.form.get("isbn")
    data=db.execute("select * from books where isbn = :isbn",{"isbn": isbn}).fetchall()
    return render_template("book.html", books=data)
    #except ValueError:
    #    return render_template("error.html",message="enter correct isbn")
