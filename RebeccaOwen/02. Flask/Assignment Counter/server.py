"""
Pajama Programmer
Coding Dojo - July 5 Online Flex
11-August-2015
Python > Flask > Assignment: Counter
"""

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

counter = 0
@app.route('/')
def index():
    global counter
    return render_template('index.html', counter=counter)

@app.route('/result', methods=['POST'])
def result():
    global counter
    if request.form['inc'] == 'Increment':
        counter += 1
    else:
        counter -= 1
    return redirect('/')


app.run(debug=True)                       # Run the app in debug mode.