import os
import pyodbc

class DatabaseConnector:
    _instance = None  # Class variable to hold the single instance

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DatabaseConnector, cls).__new__(cls)
        return cls._instance

    def __init__(self, env_var='AZURE_SQL_CONNECTIONSTRING'):
        if not hasattr(self, 'initialized'):  # Ensure initialization happens only once
            self.env_var = env_var
            self.connection = None
            self.initialized = True

    def connect(self):
        """
        Connect to the database using the connection string from the environment.
        """
        connection_string = os.environ.get(self.env_var)
        if not connection_string:
            print(f"Error: {self.env_var} environment variable not set.")
            return None

        try:
            conn = pyodbc.connect(connection_string)
            print("Successfully connected to the database.")
            self.connection = conn
        except pyodbc.Error as ex:
            print(f"Database connection error: {ex}")
            self.connection = None

        return self.connection

    def close(self):
        """
        Close the database connection if open.
        """
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
            self.connection = None