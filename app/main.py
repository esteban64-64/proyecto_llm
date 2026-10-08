from fastapi import FastAPI

from app.api.routes import chat_router, health_router

app = FastAPI(title="AI Knowledge Assistant")
app.include_router(chat_router)
app.include_router(health_router)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "AI Knowledge Assistant is running"}
