from mcp.server.fastmcp import FastMCP
import pyodbc
import os
import signal
import sys

class MCPWithDB:
    def __init__(self):
        self.mcp = FastMCP()
        self.db_connection = self._connect_to_db()
        self._register_tools()

    def _connect_to_db(self):
        """
        Connect to database
        """
        try:
            connection_string = os.environ.get("AZURE_SQL_CONNECTIONSTRING")
            print(connection_string)
            if not connection_string:
                print("Error: AZURE_SQL_CONNECTIONSTRING environment variable not set.")
                return None
            # connection = pyodbc.connect("Driver={ODBC Driver 18 for SQL Server};Server=visql-uat2501\\sql01uat;Database=CP_SALEFEED_V2;UID=develop;PWD=program@2015;TrustServerCertificate=yes")
            connection = pyodbc.connect(connection_string)
            print("Successfully connected to the database.")
            return connection
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            if sqlstate == '28000':
                print("Authentication error: Check your username and password.")
            else:
                print(f"Database connection error: {ex}")
            return None

    def _register_tools(self):
        self.mcp.tool("list_tables")(self.list_tables)

    def list_tables(self, schema_name: str = 'dbo'):
        """
        Lists all tables and views for a given schema.
        """
        if not self.db_connection:
            return {"error": "Database connection not available."}
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT table_name, table_type FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = ?", schema_name)
            tables = [{'table_name': row.table_name, 'table_type': row.table_type} for row in cursor.fetchall()]
            return tables
        except pyodbc.Error as ex:
            print(f"Error querying database: {ex}")
            return {"error": f"Failed to retrieve tables from the database for schema {schema_name}."}

    def shutdown(self):
        print("Shutting down server...")
        if self.db_connection:
            self.db_connection.close()
            print("Database connection closed.")

    def run(self):
        if self.db_connection:
            print("Starting MO MSSQL MCP server...")
            self.mcp.run(transport='stdio')
            
        else:
            print("Failed to start server due to database connection error.")

if __name__ == "__main__":
    print("Running in test mode...")
    # Ensure the connection string is set in your .env file or environment
    server = MCPWithDB()

    # Direct call to test the list_tables function
    if server.db_connection:
        print("Testing list_tables()...")
        # You can specify a schema, e.g., server.list_tables('sales')
        tables = server.list_tables()
        print("Result:")
        print(tables)

        # Cleanly close the connection after the test
        server.shutdown()
    else:
        print("Could not run test because database connection failed.")
