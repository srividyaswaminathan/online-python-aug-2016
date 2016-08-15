from flask import Flask, render_template, request
app = Flask(__name__)
app.secret_key = 'sneaky key'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    data = request.form
    print data
    return render_template('data.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
