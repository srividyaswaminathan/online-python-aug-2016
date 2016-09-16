from flask import Flask, render_template, request, redirect,flash, session

app = Flask(__name__)
app.secret_key = "SrividyaSwa"
#index.html would handle the rendering of the form
@app.route('/')
def form_render():
	return render_template("index.html")

@app.route('/index.html', methods=['POST'])
def results():
	if len(request.form['name']) <= 0:
	 	flash("Error! Please enter a valid name")
	
	print len(request.form['comment'])
	if  len(request.form['comment']) > 120  : 	
		flash("Error! Comment field cannot exceed 120 characters") 
	
	return render_template("results.html", name=request.form['name'], location=request.form['location'], language=request.form['language'], comment=request.form['comment'])
	name = request.form['name']
	location= request.form['location']
	language = request.form['language']
	comment = request.form['comment']


#run our server
app.run(debug=True)		






