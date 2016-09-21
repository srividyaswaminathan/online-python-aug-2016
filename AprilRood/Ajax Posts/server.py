from flask import Flask, render_template, request
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'posts_db')

@app.route('/')
def index():
    query = "SELECT * FROM posts"
    notes = mysql.query_db(query)
    return render_template('index.html', posts=notes)

@app.route('/posts/create', methods=['POST'])
def create():
    query = "INSERT INTO posts (note) VALUES('{}')".format(request.form['note'])
    mysql.query_db(query)
    return_query = "SELECT * FROM posts"
    posts = mysql.query_db(return_query)
    return render_template('partials/posts.html', posts=posts)

app.run(debug=True)