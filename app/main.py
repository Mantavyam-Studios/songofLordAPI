from fastapi import FastAPI
from app.routers import verses

app = FastAPI(title="Song of Lord API")

# Include verse routes
app.include_router(verses.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Song of Lord API"}