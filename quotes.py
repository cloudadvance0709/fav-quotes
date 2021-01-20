from flask import Flask , render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:chilee0709@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://chfbdgeepjzlkb:3321e5fbe11c2e99d4ed95edbf21c286a9d9e982be67786d93db65acdf6a39be@ec2-54-205-187-125.compute-1.amazonaws.com:5432/deo9pitk5ca90n'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

class Favquotes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))



@app.route('/')
def index():
    result = Favquotes.query.all()
    """fruits = ["apple", "grapes", "berries", "oranges"]"""
    """return render_template('index.html', quote='Kindness needs no translation', fruits = fruits)"""
    return render_template('index.html', result=result)

"""
@app.route('/about')
def about():
    return '<h1> Hello World from about page</h1>'
"""

@app.route('/quotes')
def quotes():
    """return '<h1> Life is a journey</h1>'"""
    return render_template('quotes.html')


@app.route('/process', methods =['POST'])
def process():
    """return '<h1> Life is a journey</h1>'"""
    author = request.form['author']
    quote = request.form['quote']
    quotedata = Favquotes(author=author, quote=quote)
    db.session.add(quotedata)
    db.session.commit()

    return redirect(url_for('index'))
