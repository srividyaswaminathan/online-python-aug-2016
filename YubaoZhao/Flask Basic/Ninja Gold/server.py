from flask import Flask, render_template, request, redirect, session
from random import randint
from  datetime import datetime
app = Flask(__name__)
app.secret_key = 'Its A Secret'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activity' not in session:
        session['activity'] = [{'status':'','log':'Welcome to Ninja Gold!'}]
    # print "Gold: %d"%session['gold']
    # print "Activities:",session['activity']
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_gold():
    data = {'farm':randint(10,20), 'cave':randint(5,10),'house':randint(2,5), 'casino':randint(-50,50)}
    building = request.form['building']
    gold = data[building]
    time = datetime.now().strftime('%Y/%m/%d %I:%M:%S %p')
    if gold > 0:
        session['activity'].append({'status':'earn','log':'Earned {} golds from the {}! ({})'.format(gold, building, time)})
    else:
        session['activity'].append({'status':'lost','log':'Entered a casino and lost %d golds... Ouch.. (%s)'%(-gold, time)})
    session['gold'] += data[building]
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('gold')
    session.pop('activity')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
