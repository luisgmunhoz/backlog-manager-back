from fastapi import Depends, FastAPI

from configs.environment import get_environment_variables
from configs.middleware import get_current_user
from metadata.tags import Tags
from models.base_model import init

# Application Environment Configuration
env = get_environment_variables()

# Core Application Instance
app = FastAPI(title=env.APP_NAME, version=env.API_VERSION, openapi_tags=Tags)


@app.get("/ping")
def ping():
    return {"message": "pong"}


@app.get("/authenticated-ping")
def authenticated_ping(user: dict = Depends(get_current_user)):
    return {"message": "pong", "user": user}


# Initialise Data Model Attributes
init()
