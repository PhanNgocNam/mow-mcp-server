import pyodbc
from services.base_service import BaseService

class SchemaService(BaseService):
    def get_schema_as_string(self, schema_name: str = 'dbo') -> str:
        """
        Explore the database schema and output it as a Markdown-formatted string.

        Args:
            schema_name: The name of the database schema to explore (default is 'dbo').
        """
        if not self.db_connection:
            return {"error": "Database connection not available."}
        try:
            cursor = self.db_connection.cursor()
            db_desc = []

            # Get Tables and Columns
             # --- Get Tables and Columns ---
            cursor.execute("""
                SELECT TABLE_NAME
                FROM INFORMATION_SCHEMA.TABLES
                WHERE TABLE_SCHEMA = ? AND TABLE_TYPE = 'BASE TABLE'
                ORDER BY TABLE_NAME
            """, schema_name)
            tables = [row.TABLE_NAME for row in cursor.fetchall()]

            for table in tables:
                db_desc.append(f"## Table: {table}")

                # --- Columns and Primary Keys ---
                cursor.execute("""
                    SELECT
                        c.COLUMN_NAME,
                        c.DATA_TYPE,
                        c.CHARACTER_MAXIMUM_LENGTH,
                        IIF(pk.CONSTRAINT_TYPE IS NOT NULL, 'primary key', NULL) as pk_info
                    FROM
                        INFORMATION_SCHEMA.COLUMNS c
                    LEFT JOIN (
                        SELECT ku.TABLE_SCHEMA, ku.TABLE_NAME, ku.COLUMN_NAME, tc.CONSTRAINT_TYPE
                        FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS AS tc
                        JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE AS ku
                          ON tc.CONSTRAINT_NAME = ku.CONSTRAINT_NAME
                        WHERE tc.CONSTRAINT_TYPE = 'PRIMARY KEY'
                    ) pk ON c.TABLE_SCHEMA = pk.TABLE_SCHEMA AND c.TABLE_NAME = pk.TABLE_NAME AND c.COLUMN_NAME = pk.COLUMN_NAME
                    WHERE c.TABLE_SCHEMA = ? AND c.TABLE_NAME = ?
                    ORDER BY c.ORDINAL_POSITION
                """, schema_name, table)

                columns_data = {}
                for row in cursor.fetchall():
                    col_def = f"{row.DATA_TYPE}"
                    if row.CHARACTER_MAXIMUM_LENGTH:
                        col_def += f"({row.CHARACTER_MAXIMUM_LENGTH})"
                    if row.pk_info:
                        col_def += f", {row.pk_info}"
                    columns_data[row.COLUMN_NAME] = {'def': col_def}

                # --- Foreign Keys ---
                cursor.execute("""
                    SELECT
                        kcu.COLUMN_NAME,
                        ccu.TABLE_NAME AS referenced_table_name,
                        ccu.COLUMN_NAME AS referenced_column_name
                    FROM
                        INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS rc
                    JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE kcu ON rc.CONSTRAINT_NAME = kcu.CONSTRAINT_NAME
                    JOIN INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE ccu ON rc.UNIQUE_CONSTRAINT_NAME = ccu.CONSTRAINT_NAME
                    WHERE kcu.TABLE_SCHEMA = ? AND kcu.TABLE_NAME = ?
                """, schema_name, table)

                for row in cursor.fetchall():
                    if row.COLUMN_NAME in columns_data:
                        columns_data[row.COLUMN_NAME]['fk'] = f"→ {row.referenced_table_name}({row.referenced_column_name})"

                # --- Format Columns ---
                for name, data in columns_data.items():
                    fk_info = data.get('fk', '')
                    if fk_info:
                        db_desc.append(f"- **{name}**: {data['def']}, foreign key {fk_info}")
                    else:
                        db_desc.append(f"- **{name}**: {data['def']}")

                # --- Indexes ---
                cursor.execute("""
                    SELECT i.name AS index_name, COL_NAME(ic.object_id, ic.column_id) AS column_name
                    FROM sys.indexes i
                    INNER JOIN sys.index_columns ic ON i.object_id = ic.object_id AND i.index_id = ic.index_id
                    INNER JOIN sys.objects o ON i.object_id = o.object_id
                    WHERE o.name = ? AND o.schema_id = SCHEMA_ID(?) AND i.is_primary_key = 0
                """, table, schema_name)
                indexes = {}
                for row in cursor.fetchall():
                    indexes.setdefault(row.index_name, []).append(row.column_name)

                if indexes:
                    db_desc.append("- **Indexes**:")
                    for index_name, cols in indexes.items():
                        db_desc.append(f"  - `{index_name}` on ({', '.join(cols)})")

                db_desc.append("")  # Blank line for spacing

            # --- Get Views ---
            cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.VIEWS WHERE TABLE_SCHEMA = ?", schema_name)
            views = [row.TABLE_NAME for row in cursor.fetchall()]
            if views:
                db_desc.append("## Views")
                for view in views:
                    db_desc.append(f"- {view}")
                db_desc.append("")

            # --- Get Stored Procedures ---
            cursor.execute("SELECT ROUTINE_NAME FROM INFORMATION_SCHEMA.ROUTINES WHERE ROUTINE_TYPE = 'PROCEDURE' AND ROUTINE_SCHEMA = ?", schema_name)
            sprocs = [row.ROUTINE_NAME for row in cursor.fetchall()]
            if sprocs:
                db_desc.append("## Stored Procedures")
                for sproc in sprocs:
                    db_desc.append(f"- {sproc}")
                db_desc.append("")

            # --- Write to File ---
            final_content = "\n".join(db_desc)
            return final_content
        except pyodbc.Error as ex:
            print(f"Error querying database: {ex}")
            return {"error": "Failed to explore database schema."}

    def get_specific_table_schema_as_string(self, tables: list[str], schema_name: str = 'dbo') -> str:
        """
        Explore the database schema and output it as a Markdown-formatted string.

        Args:
            schema_name: The name of the database schema to explore (default is 'dbo').
            tables: a list of given tables for exploring.
        """
        if not self.db_connection:
            return {"error": "Database connection not available."}
        try:
            cursor = self.db_connection.cursor()
            db_desc = []

            for table in tables:
                db_desc.append(f"## Table: {table}")

                # --- Columns and Primary Keys ---
                cursor.execute("""
                    SELECT
                        c.COLUMN_NAME,
                        c.DATA_TYPE,
                        c.CHARACTER_MAXIMUM_LENGTH,
                        IIF(pk.CONSTRAINT_TYPE IS NOT NULL, 'primary key', NULL) as pk_info
                    FROM
                        INFORMATION_SCHEMA.COLUMNS c
                    LEFT JOIN (
                        SELECT ku.TABLE_SCHEMA, ku.TABLE_NAME, ku.COLUMN_NAME, tc.CONSTRAINT_TYPE
                        FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS AS tc
                        JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE AS ku
                          ON tc.CONSTRAINT_NAME = ku.CONSTRAINT_NAME
                        WHERE tc.CONSTRAINT_TYPE = 'PRIMARY KEY'
                    ) pk ON c.TABLE_SCHEMA = pk.TABLE_SCHEMA AND c.TABLE_NAME = pk.TABLE_NAME AND c.COLUMN_NAME = pk.COLUMN_NAME
                    WHERE c.TABLE_SCHEMA = ? AND c.TABLE_NAME = ?
                    ORDER BY c.ORDINAL_POSITION
                """, schema_name, table.strip())

                columns_data = {}
                for row in cursor.fetchall():
                    col_def = f"{row.DATA_TYPE}"
                    if row.CHARACTER_MAXIMUM_LENGTH:
                        col_def += f"({row.CHARACTER_MAXIMUM_LENGTH})"
                    if row.pk_info:
                        col_def += f", {row.pk_info}"
                    columns_data[row.COLUMN_NAME] = {'def': col_def}

                # --- Foreign Keys ---
                cursor.execute("""
                    SELECT
                        kcu.COLUMN_NAME,
                        ccu.TABLE_NAME AS referenced_table_name,
                        ccu.COLUMN_NAME AS referenced_column_name
                    FROM
                        INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS rc
                    JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE kcu ON rc.CONSTRAINT_NAME = kcu.CONSTRAINT_NAME
                    JOIN INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE ccu ON rc.UNIQUE_CONSTRAINT_NAME = ccu.CONSTRAINT_NAME
                    WHERE kcu.TABLE_SCHEMA = ? AND kcu.TABLE_NAME = ?
                """, schema_name, table)

                for row in cursor.fetchall():
                    if row.COLUMN_NAME in columns_data:
                        columns_data[row.COLUMN_NAME]['fk'] = f"→ {row.referenced_table_name}({row.referenced_column_name})"

                # --- Format Columns ---
                for name, data in columns_data.items():
                    fk_info = data.get('fk', '')
                    if fk_info:
                        db_desc.append(f"- **{name}**: {data['def']}, foreign key {fk_info}")
                    else:
                        db_desc.append(f"- **{name}**: {data['def']}")

                # --- Indexes ---
                cursor.execute("""
                    SELECT i.name AS index_name, COL_NAME(ic.object_id, ic.column_id) AS column_name
                    FROM sys.indexes i
                    INNER JOIN sys.index_columns ic ON i.object_id = ic.object_id AND i.index_id = ic.index_id
                    INNER JOIN sys.objects o ON i.object_id = o.object_id
                    WHERE o.name = ? AND o.schema_id = SCHEMA_ID(?) AND i.is_primary_key = 0
                """, table, schema_name)
                indexes = {}
                for row in cursor.fetchall():
                    indexes.setdefault(row.index_name, []).append(row.column_name)

                if indexes:
                    db_desc.append("- **Indexes**:")
                    for index_name, cols in indexes.items():
                        db_desc.append(f"  - `{index_name}` on ({', '.join(cols)})")

                db_desc.append("")  # Blank line for spacing

            final_content = "\n".join(db_desc)
            return final_content
        except pyodbc.Error as ex:
            print(f"Error querying database: {ex}")
            return {"error": "Failed to explore database schema."}