from flask import render_template, redirect, url_for, request
from chicago import app
from chicago.models import db, Search
from chicago.forms import SearchOld, SearchNew, validators

@app.route("/")
def go_home():
    form = SearchOld()
    newform = SearchNew()
    return render_template("index.html", form=form, newform = newform)

@app.route("/searchold", methods=["GET", "POST"])
def go_search():
    form = SearchOld()
    newform = SearchNew()
    # if request.method == "POST":
    #     return search_results(form)
   #newnum = Search.query.get(new)
    #newstreet = Search.query.get(street_id)
    address = Search.query.all()
    print(address)
    #print(newnum)
    #print(newstreet)
    return render_template("index.html", form = form, newform=newform)

# @app.route("/results")
# def search_results(form):
#     results = []
#     #search_string = form.data['search']
#     if form.data['search'] == '':
#         queer = db.session.query(new)
#         results = queer.all()
#     if not results:
#         flash('Nothing found :(')
#         return render_template("index.html", form=form, newform = newform)
#     else:
#         return render_template('results.html', results=results) 

@app.route("/searchnew", methods=["GET", "POST"])
def re_search():
    form = SearchOld()
    newform = SearchNew()
    if form.validate_on_submit():
        address = Search.query.get(id)
        print(address)
    return render_template("index.html", form=form, newform = newform)

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