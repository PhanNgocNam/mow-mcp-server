import sys
from mcp.server.fastmcp import FastMCP
from db import DatabaseConnector
from typing import Dict, Any
from tools.explore_schema import ExploreSchemaTool
from tools.analyze_procedure import AnalyzeProcedureTool

class MCPWithDB:
    def __init__(self):
        self.mcp = FastMCP()
        self.db_connection = None
        self.db_analyzer_tool = None
        self.proc_analyzer_tool = None

    def setup(self):
        """
        Initializes the database connection, factories, and tools.
        """
        try:
            self.db_connection = DatabaseConnector().connect()
            self.db_analyzer_tool = ExploreSchemaTool(self.db_connection)
            self.proc_analyzer_tool = AnalyzeProcedureTool(self.db_connection)
            self._register_tools()
        except Exception as e:
            print(f"Failed to set up the server: {e}", file=sys.stderr)
            self.db_connection = None

    def _register_tools(self):
        """
        Registers the MCP tool handlers.
        """
        tools = {
            "analyze_database_schema": self._handle_explore_schema,
            "analyze_stored_procedure": self._handle_analyze_procedure,
        }

        for name, handler in tools.items():
            self.mcp.tool(name)(handler)

    def _handle_explore_schema(self, output_file_path: str, schema_name: str = "dbo") -> Dict[str, Any]:
        """
        An AI-assisted MCP tool that analyzes database schemas and outputs human-readable Markdown documentation.
        """
        return self.db_analyzer_tool.explore_to_markdown(output_file_path, schema_name)

    def _handle_analyze_procedure(self, procedure_name: str) -> dict:
        """
        MCP tool for generating LLM-friendly prompts to explain stored procedures
        """
        return self.proc_analyzer_tool.analyze(procedure_name)

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