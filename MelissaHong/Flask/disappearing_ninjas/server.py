from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
url_for = 'static'

<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> CodingDojoInc/master
ninjaturtles = {
    'blue':'leonardo.jpg',
    'orange':'michelangelo.jpg',
    'red':'raphael.jpg',
    'purple':'donatello.jpg',
    'april':'notapril.jpg'
}

<<<<<<< HEAD
>>>>>>> CodingDojoInc/master
=======
>>>>>>> CodingDojoInc/master
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninjaturtles():
    ninjaturtles = ['leonardo.jpg', 'michelangelo.jpg', 'raphael.jpg', 'donatello.jpg']
    return render_template('ninja.html', img = ninjaturtles)

@app.route('/ninja/<ninjaturtle>', methods = ['GET'])
def show(ninjaturtle):
    # '/ninja/' not showing
    print ninjaturtle
    img = []
    ninjaturtles = {'blue':'leonardo.jpg', 'orange':'michelangelo.jpg', 'red':'raphael.jpg', 'purple':'donatello.jpg', 'april':'notapril.jpg'}
    if ninjaturtle == 'blue' or ninjaturtle == 'orange' or ninjaturtle == 'red' or ninjaturtle =='purple':
<<<<<<< HEAD
<<<<<<< HEAD
        img.append(ninjaturtles[ninjaturtle])
        print img
    else:
        img.append(ninjaturtles['april'])
        print img
=======
=======
>>>>>>> CodingDojoInc/master
        img = ninjaturtles[ninjaturtle]
    else:
        img = ninjaturtles['april']

<<<<<<< HEAD
>>>>>>> CodingDojoInc/master
=======
>>>>>>> CodingDojoInc/master
    return render_template("ninja.html", img = img)

if __name__ == '__main__':
    app.run(debug=True)
