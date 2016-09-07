from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")
	# handles our form submission
	# note that above we defined our HTTP methods

@app.route('/users', methods=['POST'])
def create_user():
	print "Got Post Info"
	# don't worry about nxt lines till later
	# about forms
	name = request.form['name']
	email = request.form['email']
	# redirect back to '/' route
	return redirect('/') # note we imported redirect method above

app.run(debug=True) # run our server w/ debug mode

