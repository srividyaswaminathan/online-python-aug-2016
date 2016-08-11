from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"
# our index route will handle rendering our form

'''def counter():
    global counter
    counter += 1
    return counter'''

@app.route('/')
def index():
    session['counter'] = session['counter'] + 1
    return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route

app.run(debug=True) # run our server
