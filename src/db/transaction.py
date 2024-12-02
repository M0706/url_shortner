# from src.db.query import Query
from src.db.connect import Database
from src.utils.logging import logger

class Transaction:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.pool = None
        return cls._instance

    async def perform_tansaction(self, query_list):
        db_instance = await Database.get_instance()
        try:
            await db_instance.execute_many(query_list)
            return True
        except Exception as e:
            await db_instance.rollback_transaction()
            logger.error(f"Transaction failed: {e}")
            return False

    @classmethod
    async def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance