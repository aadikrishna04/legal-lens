from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__, static_url_path="/static")
mongo_uri = "mongodb+srv://aadikrishna04:5968Braves@waitlist.7v7s1th.mongodb.net/?retryWrites=true&w=majority"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/waitlist", methods=["POST"])
def waitlist():
    client = MongoClient(mongo_uri)
    db = client["waitlist"]
    collection = db.emails
    email_id = collection.insert_one({"email": request.form["email"]}).inserted_id
    print(email_id)
    return ""


# @app.route("/contact", methods=["POST"])
# def contact():
#     client = MongoClient(mongo_uri)
#     db = client["waitlist"]
#     collection = db.emails
#     email_id = collection.insert_one({"email": request.form["email"]}).inserted_id
#     print(email_id)
#     return ""
