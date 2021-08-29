from fastapi import FastAPI

from backend.auth.models import Base
from backend.auth.views import router as auth_router
from backend.db.database import engine

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(auth_router, prefix="/auth")


@app.get("/")
def hello():
    return "Hello world!"
