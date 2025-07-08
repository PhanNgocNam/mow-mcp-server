from mcp.server.fastmcp import FastMCP
import pyodbc
import os

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
            connection = pyodbc.connect("Driver={ODBC Driver 18 for SQL Server};Server=visql-uat2501\\sql01uat;Database=CP_SALEFEED_V2;UID=develop;PWD=program@2015;TrustServerCertificate=yes")
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
        self.mcp.tool("get_list_users")(self.get_list_users)

    def get_list_users(self):
        """
        Get list users from the database.
        Assumes a 'users' table with 'id' and 'name' columns.
        """
        if not self.db_connection:
            return {"error": "Database connection not available."}
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT id, name FROM users")
            users = [{'id': row.id, 'name': row.name} for row in cursor.fetchall()]
            return users
        except pyodbc.Error as ex:
            print(f"Error querying database: {ex}")
            return {"error": "Failed to retrieve users from the database."}

    def run(self):
        if self.db_connection:
            print("Starting MO MSSQL MCP server...")
            self.mcp.run(transport='stdio')
        else:
            print("Failed to start server due to database connection error.")

if __name__ == "__main__":
    server = MCPWithDB()
    server.run()
