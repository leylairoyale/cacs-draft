from flask import render_template, redirect, url_for, request
from chicago import app
from chicago.models import db, Address
from chicago.forms import SearchOld, SearchNew, validators
import csv
import pandas as pd
from io import TextIOWrapper

@app.route("/", methods=['GET', 'POST'])
def go_home():
    form = SearchOld()
    newform = SearchNew()
#below opens a csv file and adds it row by row to the db
    # with open('chicago\cacs_carmen_ave.csv', newline='') as csvfile:
    #     reading = csv.reader(csvfile)
    #     for row in reading:
    #         addy = Address(new_num=row[0], new_dir=row[1], new_street=row[2], old_num=row[3], old_dir=row[4], old_street=row[5], duplicate=row[6])
    #         db.session.add(addy)
    #         db.session.commit()
    return render_template("index.html", form=form, newform = newform)

# @app.route("/searchold", methods=["GET", "POST"])
# def go_search():
#     form = SearchOld()
#     newform = SearchNew()
#     oldnum = SearchOld(form.old_number.data)
#     # print(oldnum)
#     oldq = Address.query.filter_by(old_num = oldnum).first()
#     print(oldq)
#     # if oldq is None:
#     #     print("oops nah")
#     # else:
#     #     print("bananas for sale")
#     return render_template("index.html", form = form, newform=newform)

#below route is how to open the csvfile in a pandas dataframe
# @app.route("/searchold", methods=["GET", "POST"])
# def go_search():
#     form = SearchOld()
#     newform = SearchNew()
#     oldnum = SearchOld(form.old_number.data)
#     print("this is the oldnumber {}".format(oldnum))
#     df = pd.read_csv('chicago\cacs_carmen_ave.csv')
#         # reading = csv.DictReader(csvfile)
#         # add_search = pd.DataFrame.from_dict(reading)
#     print(df['old_num'][0])
#     print(df[df['new_num'] == oldnum])
#     for ad in df['old_num']:
#         if ad == SearchOld(form.old_number.data):
#             print('yes babnanas')
#             break
#         else:
#             pass
#     # testing = df[(df['old_num'] == oldnum)]
#     # print(testing)
#     # if str(oldnum) in str(add_search['old_num']):
#     #     print("yes today")
#     # else:
#     #     print("we have no bananas today")

#     return render_template("index.html", form = form, newform=newform)

@app.route("/searchold", methods=["GET", "POST"])
def go_search():
    form = SearchOld()
    newform = SearchNew()
    #below is the error, somehow
    # oldnum = SearchOld(old_num=request.form.get("old_num"))
    #other thing above was querying the database too early.
    #below you have to add .data to get what was actually in the form
    oldnum = form.old_number.data
    print(oldnum)
    test = Address.query.filter_by(old_num = str(oldnum)).first()
    print(test.new_num)

    #below opens a csv file and adds it row by row tot he db
    # with open('chicago\cacs_carmen_ave.csv', newline='') as csvfile:
    #     reading = csv.reader(csvfile)
    #     for row in reading:
    #         addy = Address(new_num=row[0], new_dir=row[1], new_street=row[2], old_num=row[3], old_dir=row[4], old_street=row[5], duplicate=row[6])
    #         db.session.add(addy)
    #         db.session.commit()
    return render_template("index.html", form = form, newform=newform)

# @app.route("/searchold", methods=["GET", "POST"])
# def go_search():
#     form = SearchOld()
#     newform = SearchNew()
#     oldnum = SearchOld(form.old_num.data)
#     with open('chicago\cacs_carmen_ave.csv', newline='') as csvfile:
#         reading = csv.DictReader(csvfile)
#         for row in reading:
#             print(row['new_num'], row['old_num'])
#             break
#     return render_template("index.html", form = form, newform=newform)


@app.route("/searchnew", methods=["GET", "POST"])
def re_search():
    form = SearchOld()
    newform = SearchNew()
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

@app.route("/notfound")
def no_go():
    return render_template("notfound.html")

@app.route("/contact")
def contact_me():
    return render_template("contact.html")