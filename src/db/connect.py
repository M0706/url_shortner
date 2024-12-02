import asyncpg
from src.utils.logging import logger
# from fastapi_asyncpg import configure_asyncpg
# from src.db.query import Query

class Database:

    async def connect(self, DATABASE_URL):
        return await asyncpg.create_pool(dsn=DATABASE_URL)

    async def disconnect(self):
        if self.pool:
            await self.pool.close()

db_instance = Database()