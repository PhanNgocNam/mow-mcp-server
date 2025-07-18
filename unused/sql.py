import pyodbc

class SqlDb:
    __instance = None
    def __init__(self, connection_string: str):
        if SqlDb.__instance != None:
            raise Exception("A database connection was provided.")
        else:
            SqlDb.__instance = self
            self.connection_string = connection_string

    @classmethod
    def get_instance(cls):
        if cls.__instance == None:
            cls()
        return cls.__instance()

    def connect(self):
        return pyodbc.connect(self.connection_string)