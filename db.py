#
# scrapt for managing database operations/transactions
#

from pymongo import MongoClient
from config import *
from flask import jsonify
import traceback

import json
from bson import ObjectId

######################################################
#                                                    #
# Note: _id of mongodb collection was not getting    #
# json encoded, so had to create this json encoder   #
#                                                    #
######################################################
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


class Mdb:

    def __init__(self):
        conn_str = "mongodb://%s:%s@%s:%d/%s" \
                   % (DB_USER, DB_PASS, DB_HOST, DB_PORT, AUTH_DB_NAME)
        client = MongoClient(conn_str)
        self.db = client[DB_NAME]


    def add_todo(self, title, date, done):
        try:
            rec = {
                'item': title,
                'date': date,
                'done': done
            }
            self.db.todo.insert(rec)
        except Exception as exp:
            print "add_todo() :: Got exception: %s", exp
            print(traceback.format_exc())

    def get_todo_by_title(self, title):
        collection = self.db["todo"]
        result = collection.find({"item" : title})
        if not result:
            print "invalid user"
            return "invalid user"

        todos = []
        for data in result:
            print "<<=====got the data====>> :: %s" % data
            todos.append(data)
        return jsonify({'todos': todos})


    def get_all_todo(self):
        collection = self.db["todo"]
        result = collection.find({})

        ret = []
        for data in result:
            print "<<=====got the data====>> :: %s" % data
            ret.append(data)
        return JSONEncoder().encode({'todos': ret})

if __name__ == "__main__":
    mdb = Mdb()
