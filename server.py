from flask import Flask, render_template, request
import traceback
from db import Mdb
import json


app = Flask(__name__)
mdb = Mdb()


@app.route("/")
def index():
    template_data = {'title': 'home page'}
    return render_template('index.html', **template_data)


#################################################
#                                               #
#                    ADD_TODO                   #
#                                               #
#################################################
@app.route("/add_todo", methods=['POST'])
def add_todo():
    try:
        ret = {"error": 0}
        title = request.form['title']
        description = request.form['description']
        date = request.form['date']
        done = request.form['done']
        mdb.add_todo(title, description, date, done)
        ret["msg"] = "todo added sucessfully"
    except Exception as exp:
        print "todo_done() :: Got exception: %s" % exp
        print(traceback.format_exc())
    return json.dumps(ret)


#################################################
#                                               #
#               get_all_todos                   #
#                                               #
#################################################
@app.route("/get_all_todo", methods=['GET'])
def get_all_todo():
    return mdb.get_all_todo()


#################################################
#                                               #
#                delete_todos                   #
#                                               #
#################################################
@app.route("/delete_todo", methods=['POST'])
def delete_todo():
    try:
        title = request.form['title']
        mdb.delete_todo(title)
    except Exception as exp:
        print "delete_done() :: Got exception: %s" % exp
        print(traceback.format_exc())
    return "%s" % mdb.delete_todo(title)

#################################################
#                                               #
#            get_all_pending_todo               #
#                                               #
#################################################


#################################################
#                                               #
#             get_all_done_todo                 #
#                                               #
#################################################


#################################################
#                                               #
#             Main Server                       #
#                                               #
#################################################
if __name__ == '__main__':
    app.run(debug=True)
