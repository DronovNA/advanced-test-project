from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from app.config import get_settings
from app.database import engine, Base
from app.api.rest import router as rest_router
from app.api.websocket.tasks import websocket_endpoint

logger = logging.getLogger(__name__)
settings = get_settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()

app = FastAPI(
    title="Advanced Test Project",
    description="Full-stack application with comprehensive testing",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(rest_router, prefix="/api/v1", tags=["API v1"])

@app.websocket("/ws/tasks/{user_id}")
async def websocket_tasks(websocket: WebSocket, user_id: int):
    await websocket_endpoint(websocket, user_id)

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/")
async def root():
    return {"message": "Advanced Test Project API", "version": "1.0.0"}