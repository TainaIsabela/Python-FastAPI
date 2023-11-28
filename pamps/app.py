from fastapi import FastAPI
from .routes import main_router
app = FastAPI(
    title="Pamps",
    version="0.1.0",
    description="Pamps is a posting app",
)

@app.get("/")
async def index():
    return {"Hello": "World"}

app.include_router(main_router)