import sys
import pyodbc
from services.base_service import BaseService

class ProcedureService(BaseService):
    def get_procedure_definition(self, procedure_name: str) -> str | None:
        """
        Fetches the definition of a stored procedure from the database.
        """
        if not self.db_connection:
            print("Error: Database connection not available.", file=sys.stderr)
            return None
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT definition FROM sys.sql_modules WHERE object_id = OBJECT_ID(?)"
            cursor.execute(query, procedure_name)
            row = cursor.fetchone()
            cursor.close()
            if row:
                return row.definition
            else:
                print(f"Error: Procedure '{procedure_name}' not found.", file=sys.stderr)
                return None
        except pyodbc.Error as ex:
            print(f"Database query error: {ex}", file=sys.stderr)
            return None