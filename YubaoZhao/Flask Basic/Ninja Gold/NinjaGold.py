from flask import Flask, render_template, request, redirect, session
from random import randint
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'Its A Secret'

@app.route('/')
def index():
    try:
        session['gold']
    except:
        session['gold'] = 0
    try:
        session['activity']
    except:
        session['activity'] = []
    # print "Gold: %d"%session['gold']
    # print "Activities: %s"%session['activity']
    length = len(session['activity'])
    return render_template("index.html",length=length)

@app.route('/process_money', methods=['POST'])
def process_gold():
    data = {'farm':randint(10,20), 'cave':randint(5,10),'house':randint(2,5), 'casino':randint(-50,50)}
    gold = data[request.form['building']]
    if gold > 0:
        session['activity'].append('earn')
        session['activity'].append('Earned {} golds from the {}! ({})'.format(gold,str(request.form['building']), datetime.now().strftime('%Y/%m/%d %H:%M:%S')) )
    else:
        session['activity'].append('lost')
        session['activity'].append('Entered a casino and lost %d golds... Ouch.. (%s)'%(gold, datetime.now().strftime('%Y/%m/%d %H:%M:%S')) )
    session['gold'] += data[request.form['building']]
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('gold')
    session.pop('activity')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
