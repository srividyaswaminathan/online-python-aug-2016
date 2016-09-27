from flask import Flask, render_template, request, redirect, session, flash, jsonify
from flask.ext.bcrypt import Bcrypt
import requests
import urllib

app = Flask(__name__)
app.secret_key = 'ADF2B64D-D02D-484F-BBA6-324C16CF457F' 
bcrypt = Bcrypt(app)
google_key = 'AIzaSyCdC6v47F-7CMId1T4_LqJWfEfqw3-Qagc'


@app.route('/', methods=['get'])
def index():
	return render_template('index.html')

@app.route('/directions', methods=["post"])
def get_directions():
	origin = request.form['origin']
	destination = request.form['destination']
	# package the post data from our form into a dictionary
	data = { 'origin':origin, 'destination':destination }
	# we then use the urlencode function to format our data to be passed through a query string
	# to the google maps api
	url = "https://maps.googleapis.com/maps/api/directions/json?"+urllib.urlencode(data)+"&sensor=false&key="+google_key
	# again we use the request.get function to send the request
	response = requests.get(url).content
	# we return the response to our client that sent the initial post request
	return response

app.run(debug=True)