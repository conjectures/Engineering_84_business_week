import pyodbc
import re


class ConnectToTable():

    # Initialise database to connect to specific table in Northwind Database
    def __init__(self, table):
        db = self._establish_connection()
        self.cursor = db.cursor()
        self.table = 'alexis' + table
        print(f"Trying to establish connection to {self.table}.")

    def get_db_version(self):
        return self.cursor.execute("SELECT @@version;")

    def create_table(self):
        # Creeate new table
        self.cursor.execute(f"SELECT * INTO {self.table} FROM Products;")

    def get_products(self):
        try:
            return self.cursor.execute(f"SELECT * FROM {self.table}").fetchall()
        except pyodbc.ProgrammingError:
            print("Table not found")

    def count_products(self, string):
        try:
            return self.cursor.execute(f"SELECT * FROM {self.table}").fetchall()
        except pyodbc.ProgrammingError:
            print("Table not found")

    def insert_record(self, item):
        # evaluate if all record fields are present
        pass

    def update_record(self, item):
        # evaluate if all record fields are present
        pass

    def delete_record(self, item):
        self.cursor.execute("DELETE FROM {} WHERE ProductName = '{}'".format(self.table, item))

    # Method that establishes connection with database
    def _establish_connection(self):
        # read credentials from file
        creds = self._get_creds()
        server = creds.get('server')
        database = creds.get('database')
        username = creds.get('username')
        password = creds.get('password')

        db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
        return db

    # Method reads credentials from file.
    def _get_creds(self):
        creds = {}
        with open('credentials.txt', 'r') as file:
            for line in file:
                # print(line)
                temp = line.strip('\n').split(':')
                creds.update({temp[0]: temp[1].lstrip()})

        return creds


def main():

    dbinstance = ConnectToTable('Products')
    # # dbinstance.create_table()
    # products = dbinstance.get_products()
    # if products:
    #     print(f"Found {len(products)} products")
    print(f'Version: {dbinstance.get_db_version()}')


if __name__ == '__main__':
    main()
