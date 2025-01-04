from fastapi import Depends, FastAPI

from configs.environment import get_environment_variables
from configs.middleware import get_current_user
from metadata.tags import Tags
from models.base_model import init
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Application Environment Configuration
env = get_environment_variables()

# Core Application Instance
app = FastAPI(title=env.APP_NAME, version=env.API_VERSION, openapi_tags=Tags)



origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/ping")
def ping():
    return {"message": "pong"}


@app.get("/authenticated-ping")
def authenticated_ping(user: dict = Depends(get_current_user)):
    return {"message": "pong", "user": user}


# Initialise Data Model Attributes
init()
