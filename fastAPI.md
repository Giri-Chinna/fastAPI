# FastAPI is a Python web-framework for building modern APIs
 - Fast (Performance)
 - Fast (Development)

# Key Notes
 * Few bugs
 * Quick and Easy
 * Robust
 * Standards

# HTTP request Methods
 * POST (create)
 * GET (read)
 * PUT (update)
 * DELETE (delete)

# Path Parameters
 - Path parameters are request parametes that have been attached to the URL
 - Path parameters are usually defined as a way to find the information based on locaion.
 - space = %20 in url
 - To find the location

# Query Parameters
 - Query parameters are request parameters that have been attached after a "?"
 - Query parameters have name=value pairs
 - Example:
    - URL: 127.0.0.1:8000/books/?category=science
 - To filter the data in the location

# POST Request Method
 - Used to create data
 - POST can have a body that has additional information that GET does not have
 - Example of Body
    {'title': 'Title Seven', 'author': 'Author Two', 'category': 'history', 'tag' : 'favorite'}

# PUT Request Method
 - Used to Update data
 - PUT can have a body that has additional information (like POST) that GET does not have
 - Example of Body
    {'title': 'Title Seven', 'author': 'Author Two', 'category': 'history', 'tag' : 'favorite'}

# DELETE Request Method
 - Used to delete data