from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ADF2B64D-D02D-484F-BBA6-324C16CF457F' 

@app.route('/', methods=['get'])
def index():
	return increment_count(1)

@app.route('/', methods=['post'])
def index_post():
	if request.form['submitbutton'] == 'Ninja':
		return increment_count(2)
	else:
		return increment_count(int(session['visit_count']) * -1)
	

def increment_count(by_multiple):
	visit_count = 0

	if session.get('visit_count') is not None:
		visit_count = int(session['visit_count'])

	visit_count += by_multiple
	session['visit_count'] = visit_count
	return render_template('index.html', title='Counter', description='Page visit counter.', visit_count=session['visit_count'])

app.run(debug=True)