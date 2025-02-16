# Manages verse-related API endpoints.
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app import crud

router = APIRouter(
    prefix="/verses",
    tags=["Verses"]
)

@router.get("/")
async def get_all_verses(db: AsyncSession = Depends(get_db)):
    return await crud.get_chapters(db)

@router.get("/chapter/{chapter_id}")
async def get_verses(chapter_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.get_verses_by_chapter(db)