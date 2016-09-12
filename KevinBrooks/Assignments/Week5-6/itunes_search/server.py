from flask import Flask, render_template, request, redirect, session, flash, jsonify
from flask.ext.bcrypt import Bcrypt
import requests

app = Flask(__name__)
app.secret_key = 'ADF2B64D-D02D-484F-BBA6-324C16CF457F' 
bcrypt = Bcrypt(app)

@app.route('/', methods=['get'])
def index():
	return render_template('index.html')

@app.route('/movie', methods=["post"])
def get_movie():
	artist = request.form['search_text'].replace(' ', '')
	url = "https://itunes.apple.com/search?term=" + artist + "&entity=musicVideo"

	# notice this is 'requests' not 'request'
	# we are using the request modules, 'get' function to send a request from our controller
	# then we use ".content" to get the content we are looking for
	response = requests.get(url).content
	
	# we then send the response back to our client which sent the initial post request
	return response

app.run(debug=True)