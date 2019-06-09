import sqlite3
import os.path
import sqlalchemy as db

class SqLiteHandler:

    def __init__(self):
        """Initialize database"""
        self.db = sqlite3.connect(os.path.dirname(__file__) + r'\user.db')

    def create_database(self):
        """create table"""
        self.db.execute("CREATE TABLE user_credentials (name, pw)")

    def add_user(self, user, pw):
        """
        Insert into user database
        Args:
            user: username
            pw:  password
        >>> Example: self.add_user(admin, admin)

        """
        self.db.execute("INSERT INTO user_credentials VALUES (?, ?)",  [user, pw])
        self.db.commit()

    def sql_query(self, table, record_name, columns):
        """
        Sql Query SELECT COLUMNS FROM TABLE WHERE RECORD NAME
        Args:
            table(str):
            record_name:(str)
            columns(str):

        Returns:
            records(sqlobj)

        """
        cursorObj = self.db.cursor()
        cursorObj.execute('SELECT {0} FROM {1} WHERE name="{2}"'.format(columns, table, record_name))
        records = cursorObj.fetchall()
        return records

class MySqlHandler:

    """Class implements sqlalcemy solutions
    used to read from data base server and perform querys"""

    def __init__(self, *args):
        """Initialize variables
        Running XAMPP with mysql server"""
        self.engine = db.create_engine('mysql+pymysql://root:''@127.0.0.1:3306/northwind', echo=True)
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()
        self.tables = db.Table(*args, self.metadata, autoload=True, autoload_with=self.engine)

    def select_query(self):
        """Perform a select table where query"""
        query = db.select([self.tables])
        print(query)
        ResultProxy = self.connection.execute(query)
        ResultSet = ResultProxy.fetchall()
        return ResultSet

    def set_store_details(self):
        """Perform a select table where query"""
        query = db.select([self.tables.columns.ProductName,
                           self.tables.columns.QuantityPerUnit,
                           self.tables.columns.UnitPrice,
                           self.tables.columns.UnitsInStock])
        print(query)
        ResultProxy = self.connection.execute(query)
        ResultSet = ResultProxy.fetchall()
        return ResultSet

    def get_column_name(self, table_name, filter = ['ProductName','QuantityPerUnit','UnitPrice','UnitsInStock']):
        """

        Args:
           table_name(str): name of the table

        Returns:

        """
        from sqlalchemy.inspection import inspect
        table = inspect(table_name)
        columns = []
        for column in table.c:
            if filter is not None:
                if column.name not in filter:
                    continue
            columns.append(column.name)
        return columns



if __name__=="__main__":
    mydb = SqLiteHandler()
    # # mydb.create_database()
    # # mydb.add_user()
    # asd = mydb.sql_query("user_credentials","admin","name,pw")
    # print(asd[0][0])
    mytest = MySqlHandler()
    print(mytest.select_query('products'))
    mytest.get_column_name('products')
