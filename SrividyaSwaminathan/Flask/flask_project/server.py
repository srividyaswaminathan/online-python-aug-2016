from flask import Flask, render_template, request, redirect

app = Flask(__name__)

#index.html would handle the rendering of the form
@app.route('/')
def form_render():
	return render_template("index.html")

@app.route('/results', methods=['POST'])
def results():
	return render_template("results.html", name=request.form['name'], location=request.form['location'], language=request.form['language'], comment=request.form['comment'])
	name = request.form['name']
	location= request.form['location']
	language = request.form['language']
	comment = request.form['comment']
	
#run our server
app.run(debug=True)		






