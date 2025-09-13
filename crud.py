from sqlalchemy.orm import Session
from models import User, Author, Book
from schemas import UserCreateSchemas, AuthorCreateSchemas, BookCreateSchemas
from auth import get_password_hash

def create_user(db: Session, user: UserCreateSchemas):
    hashed_pw = get_password_hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_author(db: Session, author: AuthorCreateSchemas):
    db_author = Author(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_authors(db: Session):
    return db.query(Author).all()

def create_book(db: Session, book: BookCreateSchemas):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session, author_id: int = None, year: int = None, available: bool = None):
    query = db.query(Book)
    if author_id:
        query = query.filter(Book.author_id == author_id)
    if year:
        query = query.filter(Book.year == year)
    if available is not None:
        query = query.filter(Book.available == available)
    return query.all()
