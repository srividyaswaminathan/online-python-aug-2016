from flask import Flask, render_template, request, redirect, session, flash, jsonify
from flask.ext.bcrypt import Bcrypt
from notesdatabase import *

app = Flask(__name__)
app.secret_key = 'ADF2B64D-D02D-484F-BBA6-324C16CF457F' 
bcrypt = Bcrypt(app)

@app.route('/', methods=['get'])
def index():
	return render_template('index.html')

@app.route('/notes/create', methods=['post'])
def notes_create():
	val = add_note(request.form['title'])
	return jsonify(val)

@app.route('/notes/post', methods=['post'])
def notes_post():
	val = update_note(request.form['id'], request.form['note'])
	return jsonify(val)

@app.route('/notes/get', methods=['get'])
def notes_get():
	val = get_notes()
	return jsonify(val)

@app.route('/notes/<note_id>/delete', methods=['post'])
def notes_delete(note_id):
	val = delete_note(note_id)
	return jsonify(val)

app.run(debug=True)