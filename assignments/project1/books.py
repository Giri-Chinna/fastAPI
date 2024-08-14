from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science', 'tag' : None},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science', 'tag' : None},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history', 'tag' : None},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math', 'tag' : None},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math', 'tag' : 'favorite'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math', 'tag' : 'favorite'}
]

@app.get("/api")
async def fisrt_api():
    return {'message': 'Hello World'}

@app.get("/books")
async def get_books():
    return BOOKS

# path parameter
@app.get("/books/my_books")
async def favourite_books():
    book_list = []
    for book in BOOKS:
        if book.get('tag') == 'favorite':
            book_list.append(book)
    return book_list

@app.get("/books/category/{category}")
async def get_book_by_category(category: str):
    return [book for book in BOOKS if book['category'] == category]

@app.get("/books/title/{book_title}")
async def get_book_by_title(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
        
# Query Parameters

@app.get("/books/")
async def read_category_by_query(category: str):
    book_list = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            book_list.append(book)
    return book_list

# Both path and query parameters
@app.get("/books/{author}/")
async def get_book_by_author_and_category(author: str, category: str):
    book_list = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold() and \
                book.get('category').casefold() == category.casefold():
            book_list.append(book)
    return book_list

# POST request Method
# {"title": "Title Seven", "author": "Author three", "category": "Physics", "tag" : null)

@app.post("/books/create_book")
async def create_book(new_book: dict = Body()):
    BOOKS.append(new_book)

# PUT request Method
# {"title": "Title Six", "author": "Author Two", "category": "Physics", "tag" : null)

@app.put("/books/update_book")
async def update_book(updated_book: dict = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book
            return {'message': 'Book updated successfully'}
        else:
            BOOKS.append(updated_book)
            return {'message': 'Book added successfully'}


# DELETE request Method
# {"title": "Title Six"}

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            BOOKS.remove(book)
            return {'message': 'Book deleted successfully'}
    return {'message': 'Book not found'}


# get books by author
@app.get("/books/author/{author}")
async def get_books_by_author(author: str):
    book_list = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            book_list.append(book)
    return book_list




