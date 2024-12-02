from fastapi import FastAPI
from src.db.connection_manager import connection_manager
from src.utils.logging import logger
from src.encoder.encoder import encoder
from src.db.database_map import TICKET_DATABASES, URL_SHORTNER_DATABASES
from src.routes.url_routes import url_router
# Create an instance of FastAPI
app = FastAPI()

app.include_router(url_router)

# Define a route
@app.post("/health")
async def read_root():
    return {"message": "App is reachable"}


@app.on_event("startup")
async def startup():
    await database_connect(TICKET_DATABASES)
    await database_connect(URL_SHORTNER_DATABASES)
    print("All database connections initialized.")

async def database_connect(database_map):
    for db_name, db_url in database_map.items():
        await connection_manager.add_database(db_url, db_name)

