import jwt
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt import PyJWTError

from configs.environment import get_environment_variables

app = FastAPI()


# Runtime Environment Configuration
env = get_environment_variables()

# Load the NEXTAUTH_SECRET from environment
NEXTAUTH_SECRET = env.NEXTAUTH_SECRET
ALGORITHM = "HS256"

# HTTP Bearer for extracting the Authorization header
auth_scheme = HTTPBearer()


def verify_jwt(token: str):
    try:
        # Decode the JWT using the secret
        return jwt.decode(token, NEXTAUTH_SECRET, algorithms=[ALGORITHM])
    except PyJWTError as err:
        raise HTTPException(status_code=401, detail="Invalid or expired token") from err


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    token = credentials.credentials
    return verify_jwt(token)  # Decode the token and get the user
