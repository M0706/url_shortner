from src.db.connection_manager import connection_manager
from src.utils.default_scheme import default_scheme

async def get_url_back(short_url):
    queries = [
        'SELECT url FROM url_shortener WHERE shorturl = $1',
        'UPDATE url_shortener SET count_accessed = count_accessed + 1 WHERE shorturl = $1'
    ]
    short_url_key = extract_key(short_url, default_scheme)
    url =  await connection_manager.get_long_url(queries, short_url_key,'urlshortner_db1')
    return {
    "response": "success",
    "long_url": url
}

def extract_key(url, prefix):
    if url.startswith(prefix):
        return url[len(prefix):].lstrip("/")  # Remove the prefix and leading slash
    raise ValueError("URL does not start with the provided prefix.")