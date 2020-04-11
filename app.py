from flask import Flask, flash, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///groceries.db'
db = SQLAlchemy(app)

class Groceries(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  item = db.Column(db.String(50), nullable=False)

@app.route('/')
def index():
  if request.method == 'POST':
    new = request.form.get('item')
    if new:
      newItem = Groceries(name=new)
      db.session.add(newItem)
      db.session.commit()

  query = Groceries.query.all()
  items = []
  #for item in query:
    

  return render_template('index.html', items=items)

if __name__ == '__main__':
  app.run(debug=True)