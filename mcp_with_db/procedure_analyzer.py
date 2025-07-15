import pyodbc

class ProcedureAnalyzer:
    """
    Builds an LLM prompt for explaining a SQL stored procedure.
    """
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def _get_procedure_definition(self, procedure_name: str) -> str | None:
        """
        Fetches the definition of a stored procedure from the database.
        """
        if not self.db_connection:
            print("Error: Database connection not available.")
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
                print(f"Error: Procedure '{procedure_name}' not found.")
                return None
        except pyodbc.Error as ex:
            print(f"Database query error: {ex}")
            return None

    def analyze(self, procedure_name: str) -> dict:
        """
        Construct a prompt that can be sent to an LLM to explain the procedure.

        Args:
            procedure_name: Name of the stored procedure.

        Returns:
            A dict containing the generated LLM prompt, or an error dict.
        """
        definition = self._get_procedure_definition(procedure_name)
        if not definition:
            return {"error": f"Could not retrieve definition for procedure '{procedure_name}'."}

        prompt = (
            "Please explain the following SQL stored procedure. Describe its main purpose, inputs, outputs, "
            "and the logic it implements.\n\n"
            f"**Stored Procedure:** `{procedure_name}`\n\n"
            f"```sql\n{definition}\n```"
        )
        return {"procedure_name": procedure_name, "prompt": prompt}