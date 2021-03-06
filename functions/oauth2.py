from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from schemas.index import TokenData
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from functions.token import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    return verify_token(token)
