from flask import Flask, render_template , request
import traceback
from db import Mdb
app = Flask(__name__)

mdb = Mdb()

@app.route("/")
def index():
    templateData = {'title' : 'home page '}
    return render_template('index.html', ** templateData)

@app.route("/a")
def find():
    templateData = {'title' : 'home page '}
    return render_template('find.html', ** templateData)

@app.route("/submit_todo", methods=['POST'])
def submit_todo():
    try:

        print "<<==========================>>\n", request.form
        title = request.form['title']
        date = request.form['date']
        done = request.form['done']

        print "Data is Coming......."
        mdb.add_todo(title, date, done)
        print "=============<<Data is saving.....>>=========="
    except Exception as exp:
        print "todo_done() :: Got exception: %s" % exp
        print(traceback.format_exc())
    return "todo done"


@app.route("/get_todo", methods=['POST'])
def get_todo():
    try:
        print "<<==========================>>\n", request.form
        title = request.form['title']
        print "Data is Coming......."
        mdb.retrive_data(title)
        print "=============<<Data is saving.....>>=========="
    except Exception as exp:
        print "get_done() :: Got exception: %s" % exp
        print(traceback.format_exc())
    return "%s" % mdb.retrive_data(title)

@app.route("/get_all_todo", methods=['GET'])
def get_all_todo():
    return mdb.get_all_todo()



if __name__ == '__main__':
    app.run(debug =True)
