from mcp.server.fastmcp import FastMCP
from db import DatabaseConnector
from mcp_with_db.schema_explorer import SchemaExplorer
from mcp_with_db.procedure_analyzer import ProcedureAnalyzer

class MCPWithDB:
    def __init__(self, connector: DatabaseConnector = None):
        self.connector = connector or DatabaseConnector()
        self.db_connection = self.connector.connect()
        self.explorer = SchemaExplorer(self.db_connection)
        self.proc_analyzer = ProcedureAnalyzer(self.db_connection)
        self.mcp = FastMCP()
        self._register_tools()

    def _register_tools(self):
        # Register schema exploration tool
        self.mcp.tool("explore_database_schema_str")(self._handle_explore_scheme_str)
        self.mcp.tool("explore_database_schema")(self._handle_explore_schema)
        # Register stored procedure analysis tool
        self.mcp.tool("analyze_stored_procedure")(self._handle_analyze_procedure)

    def _handle_explore_scheme_str(self, schema_name: str = "dbo"):
        """
        MCP tool handler for exploring the database schema.

        Returns:
        str: A string representation of the schema.
        """
        return self.explorer.explore_to_string(schema_name)
    def _handle_explore_schema(self, output_file_path: str, schema_name: str = "dbo"):
        """
        MCP tool handler for exploring the database schema and generating a Markdown-format report.
        """
        return self.explorer.explore_to_markdown(output_file_path, schema_name)

    def _handle_analyze_procedure(self, procedure_name: str):
        """
        MCP tool handler for building an LLM prompt to explain a stored procedure.
        """
        return self.proc_analyzer.analyze(procedure_name)

    def shutdown(self):
        print("Shutting down server...")
        self.connector.close()

    def run(self):
        if self.db_connection:
            print("Starting MO MSSQL MCP server...")
            self.mcp.run(transport='stdio')
        else:
            print("Failed to start server due to database connection error.")