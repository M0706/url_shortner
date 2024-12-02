from src.db.database_map import TICKET_DATABASES, URL_SHORTNER_DATABASES
from random import choice
from src.db.connection_manager import connection_manager
from src.encoder.encoder import encoder

def get_random_database_name():
    return choice(list(TICKET_DATABASES.keys()))

async def get_current_next_number():
    db_name = get_random_database_name()
    queries = [
    'SELECT "current" FROM ticket_number_tb_1 WHERE "current" < "end" FOR UPDATE',
    'UPDATE ticket_number_tb_1 SET "current" = "current" + 1 WHERE "current" < "end"'
]

    return await connection_manager.get_current_ticket(queries, db_name)

async def get_short_url_string():
    current_number = await get_current_next_number()
    return encoder.get_short_string(current_number)