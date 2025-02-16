# This file Defines database models when PostgreSQL is set up.
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import engine, AsyncSessionLocal
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Updated Chapter Model: Use 'number' as the primary key.
class Chapter(Base):
    __tablename__ = "chapters"
    number = Column(Integer, primary_key=True, index=True)  # Now the PK
    title = Column(String(255), nullable=False)
    introduction = Column(Text)
    verses = relationship("Verse", back_populates="chapter")

# Updated Verse Model: Reference Chapter's 'number' field.
class Verse(Base):
    __tablename__ = "verses"
    id = Column(Integer, primary_key=True, index=True)
    chapter_number = Column(Integer, ForeignKey("chapters.number"), nullable=False)
    number = Column(Integer, nullable=False)
    sanskrit_shloka = Column(Text, nullable=False)
    transliteration = Column(Text, nullable=False)
    translation = Column(Text, nullable=False)
    commentary = Column(Text, nullable=True)
    chapter = relationship("Chapter", back_populates="verses")