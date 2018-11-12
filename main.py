from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:1234@localhost:8888/build-a-blog'
app.config['SQLAlchemy_ECHO'] = True
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(400))

    def __init__(self, title, body):
        self.title = title
        self.body = body

posts=[]


@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        post = request.form['post']
        post.append(post)

    posts = Post.query.all()
    return render_template('home.html',title="Blog", posts=posts)

if __name__ == '__main__':
    app.run()