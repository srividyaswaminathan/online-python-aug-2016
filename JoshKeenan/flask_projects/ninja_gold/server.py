from flask import Flask, redirect, session, render_template, request
from random import randrange
app = Flask(__name__)
app.secret_key = 'CanYouKeepASecret'


@app.route('/')
# Looks for Gold and on an exception (eg. Undefined) reset page.
def index():
    try:
        session['gold']

    except:
        session['gold'] = 0
        session['activities'] = []
        session['text_color'] = []
        session['counter'] = 0
    return render_template('index.html')


@app.route('/process_money', methods=['post'])
def process():
    # Gold processing for the individual locations
    session['location'] = request.form['location']
    # Farm
    if session['location'] == 'farm':
        session['earn'] = randrange(10, 21)
        session['text_color'].append('green')
    # Cave
    elif session['location'] == 'cave':
        session['earn'] = randrange(5, 11)
        session['text_color'].append('green')
    # House
    elif session['location'] == 'house':
        session['earn'] = randrange(2, 6)
        session['text_color'].append('green')
    # Casino
    elif session['location'] == 'casino':
        session['earn'] = randrange(-50, 50)
    # Change Text color based upon win/loss
        if session['earn'] >= 0:
            session['text_color'].append('green')
        elif session['earn'] < 0:
            session['text_color'].append('red')

# Counter for printing index of activities
    session['counter'] += 1
# Push values to activities list for the log
    if session['location'] == 'casino' and session['earn'] > 0:
        session['activities'].append(
            'Went to casino and WON! ' + '+' + str(session['earn']) + ' gold!')
    elif session['location'] == 'casino' and session['earn'] < 0:
        session['activities'].append(
            'Went to casino and LOST! ' + str(session['earn']) + ' gold.')
    else:
        session['activities'].append(
            'Earned ' + str(session['earn']) + ' from ' + session['location'])

# Update total gold and redirect.
    session['gold'] += session['earn']

    return redirect('/')


# Reset!
@app.route('/reset', methods=['post'])
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
