

from pymongo import MongoClient
from config import *
import traceback
import json
from bson import ObjectId


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


#################################################
#                                               #
#                    ADD_TODO                   #
#                                               #
#################################################
    def add_todo(self, title, description, date, done):
        try:
            rec = {
                'title': title,
                'description': description,
                'date': date,
                'done': done
            }
            self.db.todo.insert(rec)
        except Exception as exp:
            print "add_todo() :: Got exception: %s", exp
            print(traceback.format_exc())


#################################################
#                                               #
#                get_all_todo                   #
#                                               #
#################################################
    def get_all_todo(self):
        collection = self.db["todo"]
        result = collection.find({})

        ret = []
        for data in result:
            print "<<=====got the data====>> :: %s" % data
            ret.append(data)
        return JSONEncoder().encode({'todo': ret})


#################################################
#                                               #
#                delete_todos                   #
#                                               #
#################################################
    def delete_todo(self, title):
        ret = []
        collection = self.db["todo"]
        collection.remove({"title": title})
        result = collection.find({})
        if not result:
            print "invalid user"
            return "invalid user"

        for data in result:
            print "<<=====got the data====>> :: %s" % data
            ret.append(data)
        return JSONEncoder().encode({'students': ret})


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


if __name__ == "__main__":
    mdb = Mdb()
