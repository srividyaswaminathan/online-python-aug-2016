"""
Pajama Programmer
Coding Dojo - July 5 Online Flex
08-September-2015
Python > API's & Ajax > Assignment: Ajax Posts
"""

class DevelopmentDBConfig(DBConfig):
    DB_USERNAME = 'root'
    DB_PASSWORD = 'root'
    DB_DATABASE_NAME = 'posts_db' # change this line to connect to our database!!!!
    DB_HOST = 'localhost'
    """ unix_socket is used for connecting with MAMP. Take this out if you aren't using MAMP """
    DB_OPTIONS = {
        'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock'
    }

routes['default_controller'] = "Posts";

from system.core.controller import *
class Posts(Controller):
    def __init__(self, action):
        super(Posts, self).__init__(action)
        self.load_model('Post')
    def index(self):
        posts = self.models['Post'].all()
        return self.load_view('posts/index.html', posts=posts)
    def index_html(self):
        posts = self.models['Post'].all()
        return self.load_view('partials/posts.html', posts=posts)
    def index_json(self):
        posts = self.models['Post'].all()
        return jsonify(posts=posts)
    def create(self):
        new_post = {
                   "post": request.form['post']
                }
        self.models['Post'].create(new_post)
        posts = self.models['Post'].all()
        return self.load_view('partials/posts.html', posts=posts)

from system.core.model import Model
class Post(Model):
    def __init__(self):
       super(Post, self).__init__()
    def all(self):
       query = "SELECT * FROM posts"
       return self.db.query_db(query)
    def create(self, new_post):
       query = "INSERT INTO posts (post, created_at, updated_at) VALUES (:post, NOW(), NOW())"
       data = { 'post': new_post['post'] }
       return self.db.query_db(query, data)