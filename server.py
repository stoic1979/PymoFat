from flask import Flask, render_template , request
import traceback
from db import Mdb


app = Flask(__name__)
mdb = Mdb()


@app.route("/")
def index():
    template_data = {'title' : 'home page '}
    return render_template('index.html', **template_data)


@app.route("/a")
def find():
    template_data = {'title' : 'home page '}
    return render_template('find.html', **template_data)


@app.route("/add_todo", methods=['POST'])
def add_todo():
    try:
        title = request.form['title']
        date = request.form['date']
        done = request.form['done']
        mdb.add_todo(title, date, done)
    except Exception as exp:
        print "todo_done() :: Got exception: %s" % exp
        print(traceback.format_exc())
    return "todo done"


@app.route("/get_todo", methods=['POST'])
def get_todo():
    try:
        title = request.form['title']
        mdb.retrive_data(title)
    except Exception as exp:
        print "get_done() :: Got exception: %s" % exp
        print(traceback.format_exc())
    return "%s" % mdb.retrive_data(title)


@app.route("/get_all_todo", methods=['GET'])
def get_all_todo():
    return mdb.get_all_todo()


if __name__ == '__main__':
    app.run(debug =True)
