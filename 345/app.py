from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Union, Literal

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

# normally would load from env
SECRET_KEY = (
    "963456d8424a9e506d82d1947774c56a2fa3cf1099315cd93e07f44dc5eea21a"  # noqa S105
)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str


class Food(BaseModel):
    id: int
    name: str
    serving_size: str
    kcal_per_serving: int
    protein_grams: float
    fibre_grams: float = 0


class User(BaseModel):
    id: int
    username: str
    password: str

    def __init__(self, **data: Any):
        data["password"] = get_password_hash(data["password"])
        super().__init__(**data)


class FoodEntry(BaseModel):
    id: int
    user: User
    food: Food
    date_added: datetime = datetime.now()
    number_servings: float


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()
food_log: Dict[int, FoodEntry] = {}

# We created an extra in memory user DB
users_db: Dict[str, User] = {}


def verify_password(plain_password, hashed_password):
    """Provided, all good"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """Provided, all good"""
    return pwd_context.hash(password)


def get_user(username: str):
    """Provided, all good"""
    if username in users_db:
        user = users_db[username]
        return user


def authenticate_user(username: str, password: str) -> Union[Literal[False], User]:
    """
    TODO: complete this function, use:
    https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
    """
    user = users_db.get(username)
    if user is None or not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta):
    """TODO: complete this function"""
    data = data.copy()
    data["exp"] = datetime.utcnow() + expires_delta
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(token: str = Depends(oauth2_scheme)):
    """TODO: complete this function"""
    credentials_exception = HTTPException(
        status_code=401, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: Optional[str] = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=username)
    if user is None:
        raise credentials_exception
    return user


@app.post("/create_user", status_code=201)
async def create_user(user: User):
    """Ignore / don't touch this endpoint, the tests will use it"""
    users_db[user.username] = user
    return user


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """TODO: complete this endpoint"""
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

# TODO: use fastapi.Depends (already imported) to add authentication tot the following endpoints ...


@app.post("/", status_code=201)
async def create_food_entry(entry: FoodEntry, current_user: User = Depends(get_current_user)):
    if entry.user.id != current_user.id:
        raise HTTPException(
            status_code=400, detail="Can only add food for current user")
    food_log[entry.id] = entry
    return entry


@app.get("/", response_model=List[FoodEntry])
async def get_foods_for_user(current_user: User = Depends(get_current_user)):
    """
    This endpoint does not take a user_id anymore, make it so that the
    food entries are filtered on logged in user.
    """
    return [
        food_entry
        for food_entry in food_log.values()
        if food_entry.user.id == current_user.id
        # filter by logged in user
    ]


@app.put("/{entry_id}", response_model=FoodEntry)
async def update_food_entry(entry_id: int, new_entry: FoodEntry, current_user=Depends(get_current_user)):
    if entry_id not in food_log:
        raise HTTPException(status_code=404, detail="Food entry not found")
    elif food_log[entry_id].user.id != current_user.id:
        raise HTTPException(
            status_code=400, detail="Food entry not owned by you")

    food_log[entry_id] = new_entry

    return new_entry


@app.delete("/{entry_id}", response_model=Dict[str, bool])
async def delete_food_entry(entry_id: int, current_user: User = Depends(get_current_user)):
    if entry_id not in food_log:
        raise HTTPException(status_code=404, detail="Food entry not found")
    elif food_log[entry_id].user.id != current_user.id:
        raise HTTPException(
            status_code=400, detail="Food entry not owned by you")

    del food_log[entry_id]

    return {"ok": True}
