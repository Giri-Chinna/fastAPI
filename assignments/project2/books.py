from typing import Optional
from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()

class Book:

    def __init__(self, id: int, title: str, author: str, description: str, rating: int, published_date:int):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date= published_date

class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not required on create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)
    description: str = Field(min_length=10, max_length=100)
    rating: int = Field(gt=-1, lt=6)
    published_date: int = Field(gt=1900, lt=2031)

    """
        To provide an example for the model in swagger.
        These will be shown in the example section of the model.
        These will the default values for the model.
        To create more descriptive request within Swagger documentation.
    """
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Add new Book",
                "author": "Add Author's name",
                "description": "provide a brief description",
                "rating": 5,
                "published_date": 2021
            }
        }
    }

BOOKS = [
    Book(id=1, title="The Great Gatsby", author="F. Scott Fitzgerald", description="The story of the fabulously wealthy Jay Gatsby and his love for the beautiful Daisy Buchanan.", rating=5, published_date=1925),
    Book(id=2, title="To Kill a Mockingbird", author="Harper Lee", description="The story of a young bird who is killed by a mockingbird.", rating=4, published_date=1960),
    Book(id=3, title="1984", author="George Orwell", description="The story of a dystopian society where the government controls everything.", rating=5, published_date=1949),
    Book(id=4, title="Pride and Prejudice", author="Jane Austen", description="The story of two people who fall in love despite their differences.", rating=4, published_date=2013),
    Book(id=5, title="The Catcher in the Rye", author="J.D. Salinger", description="A story about Rye who catches a catcher.", rating=3, published_date=1951),
    Book(id=6, title="The Hobbit", author="J.R.R. Tolkien", description="The story of a hobbit who goes on an adventure.", rating=4, published_date=1937),
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")
        
@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: int = Query(gt=-1, lt=6)):
    book_list = []
    for book in BOOKS:
        if book.rating == book_rating:
            book_list.append(book)
    return book_list


@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def read_book_by_publish_date(published_date: int = Query(gt=1900, lt=2031)):
    book_list = []
    for book in BOOKS:
        if book.published_date == published_date:
            book_list.append(book)
    return book_list    

# Validations using Pydantics

@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))

def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book

@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
    
    if not book_changed:
        raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
    
    if not book_changed:
        raise HTTPException(status_code=404, detail="Book ID not found")
