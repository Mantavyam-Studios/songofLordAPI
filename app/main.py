from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession

# Use absolute imports instead of relative
import app.models as models
import app.schemas as schemas
import app.crud as crud
from app.database import engine, AsyncSessionLocal
from app.routers import verses

# Lifespan event handler
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to run on startup
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
    yield
    # Code to run on shutdown
    await engine.dispose()

# Initialize FastAPI with lifespan
app = FastAPI(
    title="Song of Lord API",
    lifespan=lifespan,
    description="API for the Bhagvad Gita (Song of Lord)",
    version="1.0.0"
)

# Include routers
app.include_router(verses.router)

# Dependency to get async DB session
async def get_db():
    async with AsyncSessionLocal() as db:
        try:
            yield db
        finally:
            await db.close()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Song of Lord API"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}

# Only for development
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)