from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
#! BSON (Binary JSON) encoding and decoding.
from bson.objectid import ObjectId

app = Flask(__name__)

#! The username and password for mongodab database connections
client = MongoClient('localhost', 27017, username='admin', password='password')

db = client.flask_db
todos = db.todos
# ----------------------------------------------------------------


#! -------- Routes -------------------------------
@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index'))

    all_todos = todos.find()
    return render_template('index.html', todos=all_todos)

# Delete the object from the database by id
@app.post('/<id>/delete/')
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))
