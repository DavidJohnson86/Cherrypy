import sqlite3
import os.path
import sqlalchemy as db

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

class MySqlHandler:

    def __init__(self):
        # self.engine = sqlalchemy.db.create_engine('dialect+driver://user:pass@127.0.0.1:port/db')
        self.engine = db.create_engine('mysql+pymysql://root:''@127.0.0.1:3306/northwind', echo=True)
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()

    def select_query(self, *args):
        """Perform a select table where query"""
        self.products = db.Table(*args, self.metadata, autoload=True, autoload_with=self.engine)
        query = db.select([self.products])
        ResultProxy = self.connection.execute(query)
        ResultSet = ResultProxy.fetchall()
        return ResultSet

    def get_column_name(self, model):
        from sqlalchemy.inspection import inspect
        table = inspect(self.products)
        columns = []
        for column in table.c:
           columns.append(column.name)
        return columns



if __name__=="__main__":
    mydb = SqLiteHandler()
    # # mydb.create_database()
    # # mydb.insert_table()
    # asd = mydb.sql_query("user_credentials","admin","name,pw")
    # print(asd[0][0])
    mytest = MySqlHandler()
    print(mytest.select_query('products'))
    mytest.get_column_name('products')
