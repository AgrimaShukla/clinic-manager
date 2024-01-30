from jose import jwt, JWTError
from typing import Annotated
from fastapi import Depends, HTTPException
from datetime import timedelta, datetime
from fastapi.security import OAuth2PasswordBearer
from starlette import status
SECRET_KEY = 'fIqrMcrIKjZqsEZdfwne82n8YsL6F3K0'
ALGORITHM = 'HS256'

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='token')
def create_access_token(username: str, user_id: str, role: str, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id, 'role': role}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

def get_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try: 
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get('id')
        username = payload.get('username')
        role = payload.get('role')
        if user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail = "Could not validate user")
        return {'username': username, 'id': user_id, 'role': role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail = "Could not validate user")
    
user_dependency = Annotated[dict, Depends(get_user)]