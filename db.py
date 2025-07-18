import os
import pyodbc

class DatabaseConnector:
    _shared_state = {}  # Borg pattern

    def __init__(self, env_var='AZURE_SQL_CONNECTIONSTRING'):
        self.__dict__ = self._shared_state
        if not hasattr(self, 'initialized'):  # Ensure initialization happens only once
            self.env_var = env_var
            self.connection = None
            self._connection_string = os.environ.get(self.env_var)
            self.initialized = True

    def connect(self):
        """
        Connect to the database using the connection string.
        Ensures only one connection is active across all instances.
        Raises:
            ValueError: If the connection string environment variable is not set.
            pyodbc.Error: If the database connection fails.
        """
        if self.connection:
            return self.connection

        if not self._connection_string:
            raise ValueError(f"Error: {self.env_var} environment variable not set.")

        try:
            self.connection = pyodbc.connect(self._connection_string)
            print("Successfully connected to the database.")
            return self.connection
        except pyodbc.Error as ex:
            print(f"Database connection error: {ex}")
            self.connection = None
            raise

    def close(self):
        """
        Close the database connection if open.
        """
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
            self.connection = None
