import enum
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Defined Enum for supporting both languages
class LanguageEnum(enum.Enum):
    ENGLISH = "english"
    HINDI = "hindi"

class Chapter(Base):
    __tablename__ = "chapters"
    number = Column(Integer, primary_key=True, index=True)  # Primary Key
    language = Column(Enum(LanguageEnum), primary_key=True)  # Language column
    title = Column(String(255), nullable=False)
    introduction = Column(Text)
    verses = relationship("Verse", back_populates="chapter")

class Verse(Base):
    __tablename__ = "verses"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    chapter_number = Column(Integer, nullable=False)  # Chapter Number (Foreign Key)
    language = Column(Enum(LanguageEnum), nullable=False)  # Language column
    number = Column(Integer, nullable=False)  # Verse Number
    sanskrit_shloka = Column(Text, nullable=False)
    transliteration = Column(Text, nullable=False)
    translation = Column(Text, nullable=False)
    commentary = Column(Text, nullable=True)
    
    # Foreign key to match both chapter_number and language
    chapter = relationship("Chapter", back_populates="verses")
    __table_args__ = (
        ForeignKey("chapters.number", ondelete="CASCADE"),
    )