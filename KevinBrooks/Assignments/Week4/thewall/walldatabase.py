from flask import Flask
app = Flask(__name__)
app.secret_key = 'ADF2B64D-D02D-484F-BBA6-324C16CF457F' 

from flask.ext.bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# import the Connector function
from mysqlconnection import MySQLConnector
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'walldb')


def add_user(session):
	pw_hash = bcrypt.generate_password_hash(session['password'])
	sql = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at)' 
	sql += ' VALUES (:first, :last, :email, :password, NOW(), NOW()); '
	sql += " SELECT LAST_INSERT_ID() as 'id'"
	query_data = { 'first': session['first'], 'last': session['last'], 'email': session['email'], 'password': pw_hash }
	return mysql.query_db(sql, query_data)

def get_user(session):
	sql = 'SELECT * FROM users WHERE id = :user_id'
	query_data = { 'user_id': session['login_id'] }
	record = mysql.query_db(sql, query_data)
	for data in record:
		session['first'] = data['first_name']
		session['last'] = data['last_name']

def get_user_by_email(email):
	sql = 'SELECT * FROM users WHERE email = :email'
	query_data = { 'email': email }
	record = mysql.query_db(sql, query_data)
	return record

def add_message(msg, user_id):
	sql = 'INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())'
	query_data = { 'user_id': user_id, 'message' : msg }
	mysql.query_db(sql, query_data)

def get_messages():
	sql = """select m.id as 'message_id', u.first_name, u.last_name, m.message,date_format(m.created_at, '%M %D %Y') as 'message_date', cu.first_name as 'comment_first', cu.last_name as 'comment_last', c.comment, date_format(c.created_at, '%M %D %Y') as 'comment_date' from messages m
	join users u on m.user_id = u.id
	left join comments c on m.id = c.message_id
	left join users cu on c.user_id = cu.id
	order by m.created_at desc, m.id, c.created_at desc;"""

	records = mysql.query_db(sql)

	return_records = []
	new_record = {}
	comments = []
	new_comment = {}
	prev_id = 0
	for record in records:
		if prev_id != record['message_id']:
			if prev_id > 0:
				new_record['comments'] = comments
				comments = []
				return_records.append(new_record)

			new_record = {'message_id': record['message_id'], 'first_name': record['first_name'], 'last_name': record['last_name'], 'message_date': record['message_date'], 'message': record['message'], 'comments': []}
			prev_id = record['message_id']
			new_comment = {'comment_first': record['comment_first'], 'comment_last': record['comment_last'], 'comment_date': record['comment_date'], 'comment': record['comment']}
			comments.append(new_comment)
		else:
			new_comment = {'comment_first': record['comment_first'], 'comment_last': record['comment_last'], 'comment_date': record['comment_date'], 'comment': record['comment']}
			comments.append(new_comment)

	if len(comments) > 0:
		new_record['comments'] = comments
		return_records.append(new_record)

	return return_records

def add_comment(msg_id, user_id, comment):
	sql = 'insert into comments (message_id, user_id, comment, created_at, updated_at) VALUES (:message_id, :user_id, :commentdata, NOW(), NOW());'
	query_data = { 'message_id': msg_id, 'user_id': user_id, 'commentdata' : comment }
	mysql.query_db(sql, query_data)	

