from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'Its A Secret'

@app.route('/')
def counter():
    try:
        session['count']
    except:
        session['count'] = 0
    session['count'] += 1
    return render_template("index.html")

@app.route('/plus2', methods=['POST'])
def increment():
    session['count'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['count'] = 0
    return redirect('/')

if __name__ == "__main__":
    app.run()

# app.run(debug=True)
