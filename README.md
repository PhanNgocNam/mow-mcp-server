# mo-mssql-mcp

Command-line MCP server for exploring Microsoft SQL Server database schemas.

## Requirements

-   Python 3.13 or higher
-   Dependencies installed via `pip install .`

## Installation

```bash
pip install .
```

## Environment Variable

-   `AZURE_SQL_CONNECTIONSTRING`: Connection string for your Azure SQL Database.

## Usage

-   To test schema export locally:

```bash
python run.py test
```

-   To start the MCP server:

```bash
python run.py
```

The server will listen on stdio for MCP tool requests.

## Project Structure

```
.
├── mcp_with_db/
│   ├── db.py
│   ├── schema_explorer.py
│   └── server.py
├── run.py
├── pyproject.toml
└── README.md
```

## License

MIT
