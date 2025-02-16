# This file Adds functions for DB operations (Create, Read, Update, Delete).
# app/crud.py

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Chapter, Verse

# Add Chapter remains mostly the same
async def add_chapter(db: AsyncSession, number: int, title: str, introduction: str):
    chapter = Chapter(number=number, title=title, introduction=introduction)
    db.add(chapter)
    await db.commit()
    return chapter

# Updated Add Verse: Use chapter_number instead of chapter_id.
async def add_verse(db: AsyncSession, chapter_number: int, number: int,
                    sanskrit_shloka: str, transliteration: str, translation: str,
                    commentary: str):
    verse = Verse(chapter_number=chapter_number, number=number,
                  sanskrit_shloka=sanskrit_shloka,
                  transliteration=transliteration,
                  translation=translation,
                  commentary=commentary)
    db.add(verse)
    await db.commit()
    return verse

# Get Chapters
async def get_chapters(db: AsyncSession):
    result = await db.execute(select(Chapter))
    return result.scalars().all()

# Update query for getting verses by chapter:
async def get_verses_by_chapter(db: AsyncSession, chapter_number: int):
    result = await db.execute(select(Verse).where(Verse.chapter_number == chapter_number))
    return result.scalars().all()