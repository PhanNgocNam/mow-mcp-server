import os
import sys
from server import MCPWithDB
import json

def main():
    # Ensure environment variable is set
    if 'AZURE_SQL_CONNECTIONSTRING' not in os.environ:
        print("Please set the 'AZURE_SQL_CONNECTIONSTRING' environment variable.", file=sys.stderr)
        return

    server = MCPWithDB()

    # If run with "test" argument, export schema locally and exit
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        print("Testing explore_database_schema()...", file=sys.stderr)
        server.setup()
        if server.explorer:
            output_file = "db_schema_export.md"
            result = server.explorer.explore_to_markdown(output_file)
            print(f"Result: {result}", file=sys.stderr)
            if result.get("status") == "success":
                print(f"Schema exported successfully to {os.path.abspath(output_file)}", file=sys.stderr)
        server.shutdown()
    else:
        # Launch MCP server over stdio
        server.run()
        # print(json.dumps(server._handle_analyze_procedure("ps_test")))
        # print(json.dumps(server._handle_explore_schema("./final_test.md")))
        # print(json.dumps(server._handle_explore_schema_for_specific_tables_to_string("tb_order, tb_users, tb_product, tb_orderdetail")))

if __name__ == "__main__":
    main()