from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.router import project, user
from backend.database import SessionLocal, engine, Base
app = FastAPI()

Base.metadata.create_all(bind=engine)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/ping')
def ping():
  return {'message': 'pong'}

app.include_router(project.router)
app.include_router(user.router)