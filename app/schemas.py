from pydantic import BaseModel
from enum import Enum

class LanguageEnum(str, Enum):
    ENGLISH = "english"
    HINDI = "hindi"

class ChapterBase(BaseModel):
    number: int
    language: LanguageEnum
    title: str
    introduction: str

class ChapterCreate(ChapterBase):
    pass

class Chapter(ChapterBase):
    class Config:
        orm_mode = True

class VerseBase(BaseModel):
    chapter_number: int
    language: LanguageEnum
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