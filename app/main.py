from fastapi import FastAPI
from app.routers import verses

app = FastAPI(title="Song of Lord API")

# Include verse routes
app.include_router(verses.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Song of Lord API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

# Explicit entry point
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=10000)
