from src.db.connection_manager import connection_manager
from src.utils.logging import logger
from src.utils.default_scheme import default_scheme
from src.utils.create_url_helper import get_short_url_string


async def create_short_url(url):
    try:
        short_url_string = await get_short_url_string()
        query = 'INSERT INTO url_shortener (shorturl, url, count_accessed) VALUES ($1, $2, $3);'
        await connection_manager.execute('urlshortner_db1', query,short_url_string, url, 0)
        return {
            "response": "passed",
            "short_url": default_scheme+short_url_string,
            "unique_string": short_url_string
        }
    except Exception as e:
        logger.info("creation failed")
        return {
            "response": "failed" 
        }
    
    



