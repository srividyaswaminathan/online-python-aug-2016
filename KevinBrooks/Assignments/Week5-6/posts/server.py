from flask import Flask, render_template, request, redirect, session, flash, jsonify
from flask.ext.bcrypt import Bcrypt
from postsdatabase import *

app = Flask(__name__)
app.secret_key = 'ADF2B64D-D02D-484F-BBA6-324C16CF457F' 
bcrypt = Bcrypt(app)

@app.route('/', methods=['get'])
def index():
	return render_template('index.html')

@app.route('/posts/create', methods=['post'])
def posts_create():
	val = add_post(request.form['note'])
	return jsonify(val)

@app.route('/posts/get', methods=['get'])
def posts_get():
	val = get_posts()
	return jsonify(val)

app.run(debug=True)