from typing import overload, Literal
from services.schema_service import SchemaService
from services.procedure_service import ProcedureService
from db import DatabaseConnector

class ServiceFactory:
    def __init__(self):
        self._services = {
            "schema": SchemaService,
            "procedure": ProcedureService
        }
        self.conn = DatabaseConnector().connect()

    @overload
    def create(self, service_name: Literal["schema"]) -> SchemaService: ...

    @overload
    def create(self, service_name: Literal["procedure"]) -> ProcedureService: ...

    def create(self, service_name: str):
        service = self._services.get(service_name)
        if not service:
            raise ValueError(f"Unknown service type: {service_name}")
        return service(self.conn)