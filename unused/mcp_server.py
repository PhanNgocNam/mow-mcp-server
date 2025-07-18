from mcp.server.fastmcp import FastMCP
from factory.tool_factory import Tool

class MCPServer:
    def __init__(self):
        self.mcp = FastMCP()
        self._register_tool()

    def _register_tool(self):
        explore_schema_instance = Tool.create("explore_schema")
        self.mcp.tool("explore_database_schema_to_text")(explore_schema_instance.explore_schema)

    def shutdown():
        pass

    def run(self):
        self.mcp.run(transport="stdio")
