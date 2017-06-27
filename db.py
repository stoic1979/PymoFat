#
# scrapt for managing database operations/transactions
#

from pymongo import MongoClient
from config import *

import traceback


class Mdb:

    def __init__(self):
        conn_str = "mongodb://%s:%s@%s:%d/%s" \
                   % (DB_USER, DB_PASS, DB_HOST, DB_PORT, AUTH_DB_NAME)
        client = MongoClient(conn_str)
        self.db = client[DB_NAME]

    def add_todo_data(self, title, date, done):
        try:
            rec = {
                'item': title,
                'date': date,
                'done': done

            }
            self.db.add_data.insert(rec)
        except Exception as exp:
            print "add_todo() :: Got exception: %s", exp
            print(traceback.format_exc())



if __name__ == "__main__":
    mdb = Mdb()
