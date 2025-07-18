from typing import overload, Literal
from tools.explore_schema import ExploreSchemaTool
from tools.analyze_procedure import AnalyzeProcedureTool

class ToolFactory:
    def __init__(self):
        self._tools = {
            "explore_schema": ExploreSchemaTool,
            "analyze_procedure": AnalyzeProcedureTool,
        }

    @overload
    def create(self, tool_name: Literal["explore_schema"], **kwargs) -> ExploreSchemaTool: ...

    @overload
    def create(self, tool_name: Literal["analyze_procedure"], **kwargs) -> AnalyzeProcedureTool: ...

    def create(self, tool_name: str, **kwargs):
        tool = self._tools.get(tool_name)
        if not tool:
            raise ValueError(f"Unknown tool type: {tool_name}")
        return tool(**kwargs)