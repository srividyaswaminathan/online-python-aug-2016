import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PWD_REGEX_UPPER = re.compile(r'[A-Z]')
PWD_REGEX_LOWER = re.compile(r'[a-z]')

def validate_all(session):
	session['notifications'] = []
	ret = True
	ret = validate_text(session) & ret
	ret = validate_email(session) & ret
	ret = validate_password(session) & ret
	return ret

def validate_text(session):
	if len(session['first'].strip()) < 1:
		session['notifications'].append('First cannot be blank.')
	if len(session['last'].strip()) < 1:
		session['notifications'].append('Last cannot be blank.')
	if len(session['email'].strip()) < 1:
		session['notifications'].append('Email cannot be blank.')
	if len(session['password'].strip()) < 1:
		session['notifications'].append('Password cannot be blank.')

	if len(session['notifications']) > 0:
		return False

	return True

def validate_email(session):
	if not EMAIL_REGEX.match(session['email']):
		session['notifications'].append('Email is not valid.')
		return False

	return True

def validate_password(session):
	if not PWD_REGEX_UPPER.search(session['password']):
		session['notifications'].append('*Password must contain at least 1 upper case character.')
	if not PWD_REGEX_LOWER.search(session['password']):
		session['notifications'].append('*Password must contain at least 1 lower case character.')
	if session['password'] != session['confirm_password']:
		session['notifications'].append('*Confirm password did not match.')
	
	return (len(session['notifications']) == 0)
