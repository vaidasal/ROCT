# activate venv: source venv/Py3VEnv/bin/activate
# activate venv on win: venv\Scripts\activate

from fastapi import FastAPI



from fastapi.middleware.cors import CORSMiddleware
from routers import users, data_access

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4200",
    "http://localhost/docs",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

app.include_router(users.router)
app.include_router(data_access.router)


