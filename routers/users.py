from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import schemas, crud
from auth import authenticate_user, create_access_token, get_db

router = APIRouter()

@router.post("/register", response_model=schemas.UserSchemas)
async def register(user: schemas.UserCreateSchemas, db: AsyncSession = Depends(get_db)):
    db_user = await crud.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return await crud.create_user(db, user)

@router.post("/login", response_model=schemas.TokenSchemas)
async def login(form_data: schemas.UserCreateSchemas, db: AsyncSession = Depends(get_db)):
    user = await authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
