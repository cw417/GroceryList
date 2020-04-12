from flask import Flask, flash, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///groceries.db'
db = SQLAlchemy(app)


class Groceries(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  item = db.Column(db.String(50), nullable=False)
  num = db.Column(db.Integer, default=1)

@app.route('/')
def index():
  groceries = Groceries.query.all()
  return render_template('index.html', groceries=groceries)

@app.route('/add', methods=['POST'])
def add():
  item = Groceries(item=request.form['addItem'], num=request.form['addNum'])
  db.session.add(item)
  db.session.commit()
  return redirect(url_for('index'))

@app.route('/clearList', methods=['POST'])
def clearList():
  conn = sqlite3.connect('groceries.db')
  cursor = conn.cursor()
  cursor.execute('DELETE FROM groceries')
  conn.commit()
  conn.close()
  return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete():
  name = request.form['deleteItem']
  conn = sqlite3.connect('groceries.db')
  cursor = conn.cursor().execute(f"DELETE FROM groceries WHERE item='{name}'")
  conn.commit()
  conn.close()
  return redirect(url_for('index'))
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)