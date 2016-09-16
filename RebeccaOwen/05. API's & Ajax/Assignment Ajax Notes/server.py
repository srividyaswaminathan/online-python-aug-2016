"""
Pajama Programmer
Coding Dojo - July 5 Online Flex
10-September-2015
Python > API's & Ajax > Assignment: Ajax Notes
"""

from flask import Flask, render_template, request, redirect, jsonify # jsonify lets us send JSON back!
# Import MySQLConnector class from mysqlconnection.py
from connection import MySQLConnector
app = Flask(__name__)

db = MySQLConnector(app, 'notes_db')

queries = {
    'index' : "SELECT * FROM notes",
    'create' : "INSERT INTO notes (title, created_at, updated_at) VALUES (:title, NOW(), NOW())",
    'update' : "UPDATE notes SET note = :note, updated_at=NOW() WHERE id=:id",
    'delete' : "DELETE FROM notes WHERE id=:id",
}

@app.route('/')
def root():
    return redirect('/notes')

@app.route('/notes')
def index():
    query = queries['index']
    notes = db.query_db(query)
    return render_template('index.html', notes=notes)

@app.route('/notes/index_json')
def index_json():
    query = queries['index']
    posts = db.query_db(query)
    return jsonify(notes=notes)

@app.route('/notes/index_html')
def index_partial():
    query = queries['index']
    notes = db.query_db(query)
    return render_template('partials/notes.html', notes=notes)

@app.route('/notes/create', methods=['POST'])
def create():
    query = queries['create']
    data = {
        'title' : request.form['title']
    }

    note_id = db.query_db(query, data)

    query = queries['index']
    notes = db.query_db(query)

    return render_template('partials/notes.html', notes=notes)

@app.route('/notes/<id>/delete')
def destroy(id):
    query = queries['delete']
    data = {
        'id' : id
    }

    db.query_db(query, data)

    query = queries['index']
    notes = db.query_db(query)

    return render_template('partials/notes.html', notes=notes)

@app.route('/notes/<id>/update', methods=['POST'])
def update(id):

    query = queries['update']
    data = {
        'id' : id,
        'note' : request.form['note']
    }

    db.query_db(query, data)

    query = queries['index']
    notes = db.query_db(query)

    return render_template('partials/notes.html', notes=notes)

app.run(debug=True)