import sys
from services.schema_service import SchemaService
from typing import Dict, Any

class ExploreSchemaTool():
    def __init__(self, db_connection):
        self.schema_service = SchemaService(db_connection)

    def explore_to_markdown(self, output_file_path: str, schema_name: str = 'dbo') -> Dict[str, Any]:
        """
        Explores the database schema and generates a Markdown report.

        Args:
            output_file_path: The absolute path where the Markdown report will be saved.
            schema_name: The name of the database schema to explore (default is 'dbo').
        """
        if not output_file_path.endswith('.md'):
            return {"error": "Output file path must end with .md"}

        try:
            db_desc = self.schema_service.get_schema_as_string(schema_name)

            # --- Write to File ---
            with open(output_file_path, 'w', encoding='utf-8') as f:
                f.write(db_desc)

            return {"status": "success", "file_path": output_file_path}

        except IOError as e:
            print(f"Error writing to file: {e}", file=sys.stderr)
            return {"error": f"Failed to write to output file: {output_file_path}"}