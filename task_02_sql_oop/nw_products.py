import pyodbc


class ConnectToTable():

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
        pass

    def update_record(self, item):
        pass

    def delete_record(self, item):
        pass


    def _establish_connection(self):
        # read credentials from file

        db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
        return db




def main():
    dbinstance = ConnectToTable(Products)
    # dbinstance.create_table()
    products = dbinstance.get_products()
    if products:
        print(f"Found {len(products)} products")



if __name__ == '__main__':
    main()
