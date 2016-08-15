"""
Pajama Programmer
Coding Dojo - July 5 Online Flex
14-August-2015
Python > Flask > Assignment: Disappearing Ninja
"""

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninja/')
def ninja():
    session['img'] = 'img/tmnt.png'
    return render_template("ninja.html", color='TMNT')

@app.route('/ninja/<color>')
def show_ninja(color):
    color = color.lower();
    if color == 'blue':
        session['img'] = 'img/leonardo.jpg'
    elif color == 'orange':
        session['img'] = 'img/michelangelo.jpg'
    elif color == 'purple':
        session['img'] = 'img/donatello.jpg'
    elif color == 'red':
        session['img'] = 'img/raphael.jpg'
    elif color == 'ninjapajama':
        session['img'] = 'img/Becky Age 6.jpg'
    else:
        session['img'] = 'img/notapril.jpg'

    return render_template("ninja.html", color=color)

app.run(debug=True)                       # Run the app in debug mode.