from fastapi import APIRouter, FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from src.services.create_short_url import create_short_url
from src.services.get_url import get_url_back
from src.models.models import ShortURLModel, LongURLModel

url_router: APIRouter = APIRouter()


@url_router.post("/create")
async def create_shorturl_route(url_params: ShortURLModel):
    return await create_short_url(url_params.url)

@url_router.post("/get_long_url")
async def create_shorturl_route(url_params: LongURLModel):
    return await get_url_back(url_params.url)