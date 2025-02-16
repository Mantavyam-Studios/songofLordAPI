from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from . import models, schemas, crud
from .database import engine, AsyncSessionLocal

# Lifespan event handler
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to run on startup
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
    yield
    # Code to run on shutdown (optional)
    await engine.dispose()

# Initialize FastAPI with lifespan
app = FastAPI(title="Song of Lord API", lifespan=lifespan)

# Dependency to get async DB session
async def get_db():
    async with AsyncSessionLocal() as db:
        yield db

@app.get("/")
def read_root():
    return {"message": "Welcome to the Song of Lord API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}