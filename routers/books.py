import schemas, crud
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from auth import get_current_user, get_db

router = APIRouter()

@router.post("/books", response_model=schemas.BookSchemas)
async def create_book(book: schemas.BookCreateSchemas, db: AsyncSession = Depends(get_db), user=Depends(get_current_user)):
    return await crud.create_book(db, book)

@router.get("/books", response_model=list[schemas.BookSchemas])
async def list_books(author_id: int = None, year: int = None, available: bool = None, db: AsyncSession = Depends(get_db)):
    return await crud.get_books(db, author_id, year, available)
