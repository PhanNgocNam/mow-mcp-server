import sys
from mcp.server.fastmcp import FastMCP
from db import DatabaseConnector
from factory.tool_factory import ToolFactory
from typing import Dict, Any

class MCPWithDB:
    def __init__(self):
        self.mcp = FastMCP()
        self.db_connection = None
        self.explorer = None
        self.proc_analyzer = None

    def setup(self):
        """
        Initializes the database connection, factories, and tools.
        """
        try:
            self.db_connection = DatabaseConnector().connect()
            tool_factory = ToolFactory()
            self.explorer = tool_factory.create("explore_schema", db_connection=self.db_connection)
            self.proc_analyzer = tool_factory.create("analyze_procedure", db_connection=self.db_connection)
            self._register_tools()
        except Exception as e:
            print(f"Failed to set up the server: {e}", file=sys.stderr)
            self.db_connection = None

    def _register_tools(self):
        """
        Registers the MCP tool handlers.
        """
        tools = {
            "explore_database_schema(text)": self._handle_explore_scheme_str,
            "explore_database_schema(mark-down)": self._handle_explore_schema,
            "explore_database_schema_of_a_list_of_specific_tables(text)": self._handle_explore_schema_for_specific_tables_to_string,
            "analyze_stored_procedure": self._handle_analyze_procedure,
        }

        for name, handler in tools.items():
            self.mcp.tool(name)(handler)

    def _handle_explore_scheme_str(self, schema_name: str = "dbo") -> str:
        """
        MCP tool handler for exploring the database schema.

        Returns:
        str: A string representation of the schema.
        """
        return self.explorer.explore_to_string(schema_name)
    
    def _handle_explore_schema_for_specific_tables_to_string(self, tables: str, schema_name: str = "dbo") -> str:
        """
        MCP tool handler for exploring the database schema of a list of specific tables.

        Returns:
        str: A string representation of the extracted schema.
        """
        list_table = tables.split(",")
        return self.explorer.explore_specific_table_to_string(list_table, schema_name)


    def _handle_explore_schema(self, output_file_path: str, schema_name: str = "dbo") -> Dict[str, Any]:
        """
        MCP tool handler for exploring the database schema and generating a Markdown-format report.
        """
        return self.explorer.explore_to_markdown(output_file_path, schema_name)

    def _handle_analyze_procedure(self, procedure_name: str) -> dict:
        """
        MCP tool handler for building an LLM prompt to explain a stored procedure.
        """
        return self.proc_analyzer.analyze(procedure_name)

    def shutdown(self):
        """
        Shuts down the server.
        """
        print("Shutting down server...", file=sys.stderr)

    def run(self):
        """
        Runs the MCP server.
        """
        self.setup()
        if self.db_connection:
            print("Starting MO MSSQL MCP server...", file=sys.stderr)
            self.mcp.run(transport='stdio')
        else:
            print("Failed to start server due to database connection error.", file=sys.stderr)