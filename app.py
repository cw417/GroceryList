from flask import Flask, flash, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///groceries.db'
db = SQLAlchemy(app)

class Groceries(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  item = db.Column(db.String(50), nullable=False)

@app.route('/')
def index():
  groceries = Groceries.query.all()
  return render_template('index.html', groceries=groceries)

@app.route('/add', methods=['POST'])
def add():
  item = Groceries(item=request.form['addItem'])
  db.session.add(item)
  db.session.commit()
  return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(debug=True)