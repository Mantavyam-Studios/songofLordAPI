# Manages verse-related API endpoints.
from fastapi import APIRouter

router = APIRouter(
    prefix="/verses",
    tags=["Verses"]
)

# Sample endpoint
@router.get("/{verse_number}")
def get_verse(verse_number: int):
    return {
        "verse_number": verse_number,
        "sanskrit": "धर्मक्षेत्रे कुरुक्षेत्रे...",
        "translation": "In the field of dharma, Kurukshetra...",
        "explanation": "This verse sets the stage for the Gita."
    }