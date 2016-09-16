from flask import Flask, render_template, session, redirect, request
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "ThisIsSecret"
mysql = MySQLConnector(app, "full_friends_db")

#create dictionaries for queries
queries = {
            "create": "INSERT INTO friends (first_name, last_name, email, created_at) VALUES (:first_name, :last_name, :email, NOW())",
            "show": "SELECT * from friends",
            "update": "UPDATE friends SET first_name= :first_name, last_name= :last_name, email= :email WHERE id= :id",
            "get_by_id": "SELECT * from friends WHERE id= :id",
            "delete": "DELETE FROM friends WHERE id= :id"
}

#create routes
#Display all of the friends on the index.html page
@app.route("/")
def index():
    query = queries['show']
    data = {

    }
    results = mysql.query_db(query, data)
    return render_template("index.html", friends=results)
    

#  Handle the add friend form submit and create the friend in the DB
@app.route("/friends", methods=["POST"])
def create():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    query = queries['create']
    data = {
             "first_name": first_name,
             "last_name": last_name,
             "email": email   
    }
    friends= mysql.query_db(query, data)    
    return redirect('/') 

#Display the edit friend page for the particular friend
@app.route("/friends/<id>/edit", methods=["POST"])
def edit(id):
    query = queries['get_by_id']
    data = {
            'id': id
    }
    friends = mysql.query_db(query, data)
    print friends
    return render_template("edit.html", friend=friends[0])
    

#Handle the edit friend form submit and update the friend in the DB
@app.route("/friends/<id>", methods=["POST"])
def update(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    query = queries['update']
    data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'id': id
    }
    print data
    friends = mysql.query_db(query, data)
    return redirect("/")
  
#Delete the friend from the DB
@app.route("/friends/<id>/delete", methods=["POST"]) 
def destroy(id):
    query = queries['delete']
    data = {
            'id': id  
    }
    friends = mysql.query_db(query, data)
    return redirect("/")
app.run(debug=True)