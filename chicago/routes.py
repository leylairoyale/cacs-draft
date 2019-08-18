from flask import render_template, redirect, url_for, request
from chicago import app
from chicago.models import db, Address
from chicago.forms import SearchOld, SearchNew, validators
import csv

@app.route("/")
def go_home():
    form = SearchOld()
    newform = SearchNew()
    return render_template("index.html", form=form, newform = newform)

@app.route("/searchold", methods=["GET", "POST"])
def go_search():
    form = SearchOld()
    newform = SearchNew()
    with open('chicago\cacs_carmen_ave.csv', newline='') as csvfile:
        reading = csv.DictReader(csvfile)
        for row in reading:
            print(row['new_num'], row['old_num'])
            break
    return render_template("index.html", form = form, newform=newform)


@app.route("/searchnew", methods=["GET", "POST"])
def re_search():
    form = SearchOld()
    return render_template("index.html", form=form, newform = newform)

# other pages sans database stuff

@app.route("/about")
def about_me():
    return render_template("about.html")

@app.route("/friends")
def my_friends():
    return render_template("friends.html")

@app.route("/research")
def do_research():
    return render_template("research.html")

@app.route("/contact")
def contact_me():
    return render_template("contact.html")