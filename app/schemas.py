# This file Creates Pydantic models for data validation
# app/schemas.py

from pydantic import BaseModel

# Chapter Schemas
class ChapterBase(BaseModel):
    number: int
    title: str
    introduction: str

class ChapterCreate(ChapterBase):
    pass

class Chapter(ChapterBase):
    class Config:
        orm_mode = True

# Verse Schemas
class VerseBase(BaseModel):
    chapter_number: int
    number: int
    sanskrit_shloka: str
    transliteration: str
    translation: str
    commentary: str

class VerseCreate(VerseBase):
    pass

class Verse(VerseBase):
    id: int

    class Config:
        orm_mode = True