class SqlDatabase:
    debug: bool
    home: str
    version: float
    database: str
    schema: str
    table: str
    sql_insert: str
    sql_query: str
    dataq: list[dict]
    db_version: str
    def __init__(
        self, database: str, table: str, insert: str, schema: str = ..., debug: bool = ...
    ) -> None: ...
    def queue(self, data: dict) -> None: ...
    def insert(self, method: str = ..., index: str = ...) -> None: ...
    def latest_datapoint(self) -> str: ...
