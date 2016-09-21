from flask import Flask, render_template, session, redirect, request, jsonify
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'ajax_posts') 

queries = {
			"show": "SELECT * from posts",
			"create": "INSERT INTO posts (description, created_at, updated_at) VALUES (:description, NOW(), NOW())",	
			
}

@app.route("/posts")
def index():
	query = queries['show']
	posts = mysql.query_db(query)
	print "showing posts", posts
	return render_template("index.html", posts=posts)


@app.route("/posts/create", methods=["POST"])
def create_posts():
	post_description = request.form['post_description']
	query = queries['create']
	data = {
			'description': post_description
	}

	mysql.query_db(query,data)
	print "creating new post"
	# return redirect("/posts")
	query = queries['show']
	posts = mysql.query_db(query)
	print "before returning json", posts
	return jsonify(posts=posts)


app.run(debug=True)


