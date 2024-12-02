from src.db.connect import db_instance
from src.utils.logging import logger


class ConnectionManager:
    def __init__(self):
        self.pools = {}
    
    async def add_database(self, db_url, db_name):
        self.pools[db_name] = await db_instance.connect(db_url)

    async def get_pool(self, connection_name):
        if connection_name in self.pools:
            return self.pools[connection_name]
        raise ValueError(f"No pool found for database: {connection_name}")
    
    async def execute(self, connection_name, query: str, *args):
        connection_pool = await self.get_pool(connection_name)
        print("reached here")
        async with connection_pool.acquire() as connection:
            return await connection.execute(query, *args)

    async def fetch(self,connection_name, query: str, *args):
        connection_pool = await self.get_pool(connection_name)
        async with connection_pool.acquire() as connection:
            return await connection.fetch(query, *args)

    async def execute_many(self, queries, connection_name):
        connection_pool = await self.get_pool(connection_name)
        print(connection_pool)
        async with connection_pool.acquire() as connection:
            logger.info(queries)
            async with connection.transaction():
                for query, args in queries:
                    print(f"query: {query}, Args: {args}")
                    await connection.execute(query, *args)

                print("transaction succesful")
    
    async def get_current_ticket(self, queries, connection_name):
        connection_pool = await self.get_pool(connection_name)
        print(connection_pool, connection_name)
        async with connection_pool.acquire() as connection:
            async with connection.transaction():
                try:
                    current = await connection.fetchval(queries[0])  # SELECT query
                    if current is not None:
                        await connection.execute(queries[1])  # UPDATE query 
                    return current
                except Exception as e:
                    print(f"Transaction failed, rolled back. Error: {e}")
                    return None

    async def get_long_url(self, queries, short_url, connection_name):
        connection_pool = await self.get_pool(connection_name)
        print(connection_pool, connection_name)
        async with connection_pool.acquire() as connection:
            async with connection.transaction():
                try:
                    url = await connection.fetchval(queries[0], short_url)  # SELECT query
                    if url is not None:
                        await connection.execute(queries[1], short_url)  # UPDATE query 
                    return url
                except Exception as e:
                    print(f"Transaction failed, rolled back. Error: {e}")
                    return None


    async def rollback_transaction(self):
        async with self.pool.acquire() as connection:
            await connection.rollback()
    

connection_manager = ConnectionManager()