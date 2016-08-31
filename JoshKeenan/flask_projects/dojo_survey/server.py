from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'sneaky key'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    data = request.form
    error = False
    if len(request.form['about']) == 0:
        error = True
        session['about_err'] = "Cannot be blank"
    if len(request.form['name']) == 0:
        error = True
        session['name_err'] = "Cannot be blank"
    if len(request.form['about']) > 121:
        error = True
        session['about_err'] = " Must be less than 120 characters"
    if error:
        return redirect('/')
    session.pop('name_err')
    session.pop('about_err')
    return render_template('data.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
