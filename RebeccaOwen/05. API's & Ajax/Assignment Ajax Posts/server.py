"""
Pajama Programmer
Coding Dojo - July 5 Online Flex
08-September-2015
Python > API's & Ajax > Assignment: Ajax Posts
"""

from flask import Flask, render_template, request, redirect, jsonify # jsonify lets us send JSON back!
# Import MySQLConnector class from mysqlconnection.py
from connection import MySQLConnector
app = Flask(__name__)

db = MySQLConnector(app, 'posts_db')

queries = {
    'index' : "SELECT * FROM posts",
    'create' : "INSERT INTO posts (post, created_at, updated_at) VALUES (:post, NOW(), NOW())"
}

@app.route('/')
def root():
    return redirect('/posts')

@app.route('/posts')
def index():
    query = queries['index']
    posts = db.query_db(query)
    return render_template('index.html', posts=posts)

@app.route('/posts/index_json')
def index_json():
    query = queries['index']
    posts = db.query_db(query)
    return jsonify(posts=posts)

@app.route('/posts/index_html')
def index_partial():
    query = queries['index']
    posts = db.query_db(query)
    return render_template('partials/posts.html', posts=posts)

@app.route('/posts/create', methods=['POST'])
def create():
    query = queries['create']
    data = {
        'post' : request.form['post']
    }
    post_id = db.query_db(query, data)

    query = queries['index']
    posts = db.query_db(query)

    return render_template('partials/posts.html', posts=posts)

app.run(debug=True)