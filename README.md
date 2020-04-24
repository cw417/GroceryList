# GroceryList
Python Flask grocery list app

## Table of Contents
1. Getting Started
    1. Prerequisites
    2. Installing
2. How to Use
3. How It Works
4. Built With
5. Acknowledgements

## Getting Started
These steps will get GroceryList running on a local Flask server that can be accessed on your home network.

### Prerequisites
- Python 3.6+
- Python dependencies:
    - flask
    - flask-sqlalchemy
- SQLite 3

### Installing
1. Install the necessary Python libraries with:
`pip install flask flask_sqlalchemy`

2. Download the sqlite3 executable and place it in the same folder as "app.py":
`https://sqlite.org/download.html`

3. Create a database to store your data:
`sqlite3 groceries.db`
`.tables`

4. Create table data in sqlite3 database from class in "app.py":
`from app import db`
`db.create_all()`

5. Run "app.py":
`python3 app.py`

6. Access the application by using your browser of choice to go to:
`127.0.0.1:5000`

### How to Use
- Enter the name and number of the item you wish to add to the grocery list under the "Add Item" section, and press "Add".
- If you want to delete an item from the list, enter the full name of the item as it is listed into the "Delete Item" section, and press "Delete".
- To clear the entire list of all entries, press the "Clear" button in the "Clear List" section.

## How It Works
- GroceryList uses the Python miro web framework Flask to render HTML and CSS, with functionality written in Python.
- Item data is stored in a SQLite 3 database.
- Flask-SQLAlchemy interfaces with the SQLite 3 database where the items are stored, queried, and deleted.


## Built With
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Python micro web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - Python SQL toolkit and ORM
- [SQLite 3](https://sqlite.org/index.html) - Database

## Acknowledgments
- PrettyPrinted's [Flask tutorial](https://youtu.be/lWA0GgUN8kg)