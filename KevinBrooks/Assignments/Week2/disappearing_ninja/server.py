from flask import Flask, render_template, request, redirect, session
#import logging
#logging.basicConfig(filename='site.log',level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = 'ADF2B64D-D02D-484F-BBA6-324C16CF457F' 

@app.route('/', methods=['get'])
def index():
	return render_template('index.html')
	
@app.route('/ninja/', methods=['get'])
def ninja_get():
	return render_template('ninja.html', pic="/static/img/ninjas/tmnt.png")

@app.route('/ninja/<ninja_type>', methods=['get'])
def ninja(ninja_type):
	if ninja_type.lower() == 'blue':
		return render_template('ninja.html', pic="/static/img/ninjas/leonardo.jpg")
	elif ninja_type.lower() == 'red':
		return render_template('ninja.html', pic='/static/img/ninjas/raphael.jpg')
	elif ninja_type.lower() == 'orange':
		return render_template('ninja.html', pic='/static/img/ninjas/michelangelo.jpg')
	elif ninja_type.lower() == 'purple':
		return render_template('ninja.html', pic='/static/img/ninjas/donatello.jpg')
	else:
		return render_template('ninja.html', pic='/static/img/ninjas/notapril.jpg')


app.run(debug=True)