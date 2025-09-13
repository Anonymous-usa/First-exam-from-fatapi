import uvicorn

from fastapi import FastAPI

from routers import authors, books, users

app = FastAPI(debug=True)

app.include_router(users.router, tags=["Users"])
app.include_router(books.router, tags=["Books"])
app.include_router(authors.router, tags=["Authors"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)