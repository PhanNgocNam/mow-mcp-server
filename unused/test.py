import sys
from pathlib import Path

# Add the parent directory to sys.path to allow imports
sys.path.append(str(Path(__file__).parent.parent))

from factory.service_factory import ServiceFactory

def main():
    schema = ServiceFactory().create("schema")
    print(schema.get_schema_as_string("dbo"))

if __name__ == "__main__":
    main()