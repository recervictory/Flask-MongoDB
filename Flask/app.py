import os

from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
#! BSON (Binary JSON) encoding and decoding.
from bson.objectid import ObjectId

app = Flask(__name__)

print("🧩 Host: " + str(os.getenv('HOST')))
#! The username and password for mongodab database connection
try:
    if os.getenv('HOST') =='mongodb':
        client = MongoClient("mongodb://admin:password@mongo:27017")
    else:
        client = MongoClient('localhost', 27017, username='admin', password='password')
    db = client.flask_db
    todos = db.todos
    print("✅ Successfully connected to MongoDB database!")
except:
    print("❌ Failed to connect to MongoDB database.")

'''
* Alternatively Can Written
client = MongoClient(host='mongo',
                    port=27017, 
                    username='admin', 
                    password='password',
                    authSource="admin")
'''


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


#! Run the main application
if __name__ == '__main__':
    #define the localhost ip and the port that is going to be used
    # in some future article, we are going to use an env variable instead a hardcoded port 
    app.run(host='0.0.0.0', port=os.getenv('PORT'))