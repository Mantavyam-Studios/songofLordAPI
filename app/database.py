import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
load_dotenv()

# Get connection string from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Create Async Engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Session Factory
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Dependency to get DB session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session