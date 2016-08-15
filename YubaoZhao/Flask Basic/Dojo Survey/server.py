from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    username = request.form['username']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    return render_template("result.html",username=username,location=location,language=language,comment=comment)

app.run(debug=True)
