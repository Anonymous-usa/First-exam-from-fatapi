from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from auth import get_current_user, get_current_admin, get_db
import schemas, crud

router = APIRouter()

@router.post("/authors", response_model=schemas.AuthorSchemas)
async def create_author(author: schemas.AuthorCreateSchemas, db: AsyncSession = Depends(get_db), user=Depends(get_current_admin)):
    return await crud.create_author(db, author)

@router.get("/authors", response_model=list[schemas.AuthorSchemas])
async def list_authors(db: AsyncSession = Depends(get_db)):
    return await crud.get_authors(db)

