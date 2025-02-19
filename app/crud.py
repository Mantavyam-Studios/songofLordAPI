# This file Adds functions for DB operations (Create, Read, Update, Delete)
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Chapter, Verse, LanguageEnum

async def add_chapter(db: AsyncSession, number: int, language: LanguageEnum, title: str, introduction: str):
    chapter = Chapter(number=number, language=language, title=title, introduction=introduction)
    db.add(chapter)
    await db.commit()
    return chapter

async def add_verse(db: AsyncSession, chapter_number: int, language: LanguageEnum, number: int,
                    sanskrit_shloka: str, transliteration: str, translation: str, commentary: str):
    verse = Verse(chapter_number=chapter_number, language=language, number=number,
                  sanskrit_shloka=sanskrit_shloka,
                  transliteration=transliteration,
                  translation=translation,
                  commentary=commentary)
    db.add(verse)
    await db.commit()
    return verse

async def get_chapters(db: AsyncSession, language: LanguageEnum):
    result = await db.execute(select(Chapter).where(Chapter.language == language))
    return result.scalars().all()

async def get_verses_by_chapter(db: AsyncSession, chapter_number: int, language: LanguageEnum):
    result = await db.execute(select(Verse).where(Verse.chapter_number == chapter_number, Verse.language == language))
    return result.scalars().all()