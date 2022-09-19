import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db import generate_schema, init_db


from app.api.api import api_router
from app.config import settings
from app.debugger import initialize_fastapi_server_debugger_if_needed

log = logging.getLogger("uvicorn.info")


def create_application():
    initialize_fastapi_server_debugger_if_needed()

    app = FastAPI(
        title=settings.TITLE,
        description=settings.DESCRIPTION,
        version=settings.VERSION,
    )
    app.include_router(api_router, prefix="/api")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)
    await generate_schema()
