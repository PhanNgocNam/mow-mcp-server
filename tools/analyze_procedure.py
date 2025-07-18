from tools.base_tool import BaseTool
from services.procedure_service import ProcedureService

class AnalyzeProcedureTool(BaseTool):
    def __init__(self, db_connection):
        super().__init__()
        self.procedure_service = ProcedureService(db_connection)

    def analyze(self, procedure_name: str) -> dict:
        """
        Construct a prompt that can be sent to an LLM to explain the procedure.

        Args:
            procedure_name: Name of the stored procedure.

        Returns:
            A dict containing the generated LLM prompt, or an error dict.
        """
        definition = self.procedure_service.get_procedure_definition(procedure_name)
        if not definition:
            return {"error": f"Could not retrieve definition for procedure '{procedure_name}'."}

        prompt = (
            "Please explain the following SQL stored procedure. Describe its main purpose, inputs, outputs, "
            "and the logic it implements.\n\n"
            f"**Stored Procedure:** `{procedure_name}`\n\n"
            f"```sql\n{definition}\n```"
        )
        return {"procedure_name": procedure_name, "prompt": prompt}