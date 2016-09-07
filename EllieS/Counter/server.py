from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key= 'thisIsSecret'

@app.route('/')
def counter():
    session['counter'] += 1
    return render_template("index.html", counter=session["counter"])

@app.route('/increment')
def increment():
    session['counter']+=1
    return redirect('/')
@app.route('/reset')
def reset():
    session['counter'] = 0
    return redirect('/')

app.run(debug=True)
