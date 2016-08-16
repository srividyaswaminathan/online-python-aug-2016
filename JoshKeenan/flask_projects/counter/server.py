from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = "super secret"


@app.route('/')
def counter():
    try:
        session['counter']
    except:
        session['counter'] = 0
    session['counter'] += 1
    return render_template('index.html')


@app.route('/reset', methods=['POST'])
def reset():
    session['counter'] = 0
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
