import sqlite3
import os.path

class SqLiteHandler:

    def __init__(self):
        self.db = sqlite3.connect(os.path.dirname(__file__) + r'\user.db')

    def create_database(self):
        self.db.execute("CREATE TABLE user_credentials (name, pw)")

    def insert_table(self):
        self.db.execute("INSERT INTO user_credentials VALUES (?, ?)",  ["admin","adnin" ])
        self.db.commit()

    def sql_query(self, table, record_name, columns):
        cursorObj = self.db.cursor()
        cursorObj.execute('SELECT {0} FROM {1} WHERE name="{2}"'.format(columns, table, record_name))
        records = cursorObj.fetchall()
        return records

if __name__=="__main__":
    mydb = SqLiteHandler()
    # mydb.create_database()
    # mydb.insert_table()
    asd = mydb.sql_query("user_credentials","admin","name,pw")
    print(asd[0][0])