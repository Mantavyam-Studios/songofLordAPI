import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Get connection string from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Ensure the URL uses the asyncpg driver and remove sslmode
if DATABASE_URL:
    # Handle "postgres://" and "postgresql://" formats
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+asyncpg://")
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")
    # Remove sslmode parameter
    DATABASE_URL = DATABASE_URL.split("?")[0]
else:
    raise ValueError("DATABASE_URL not found in environment variables")

# Create Async Engine
engine = create_async_engine(
    DATABASE_URL, 
    echo=True, 
)

# Session Factory
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Dependency to get DB session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session