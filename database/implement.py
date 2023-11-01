from . import base


class PostgreSQL(base.TransactionDatabase):
    @property
    def interface(self):
        return "psycopg2"


class AsyncPostgreSQL(base.AsyncDatabase):
    @property
    def interface(self):
        return "asyncpg"


class SQLite(base.FileDatabase):
    pass