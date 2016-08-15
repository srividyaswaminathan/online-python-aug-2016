from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninja')
@app.route('/ninja/<color>')
def ninja(color=None):
    turtle = {'blue':'leonardo.jpg','orange':'michelangelo.jpg','red':'raphael.jpg','purple':'donatello.jpg'}
    ninja = {}

    if color == None:
        ninja = turtle
    elif color == 'blue' or color == 'orange' or color == 'red' or color =='purple':
        ninja[color] = turtle[color]
    else:
        ninja['megan'] = 'notapril.jpg'
    print ninja
    return render_template("turtles.html",ninja=ninja)

if __name__ == '__main__':
    app.run(debug=True)
