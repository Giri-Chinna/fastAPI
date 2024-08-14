# What is Pydantics?
- Python library that is used for data modeling, data parsing and has efficient error handling.
- Pydantics is commonly used as a resource for data validation and how to handle data coming to our FastAPI application.

# Implementation
- Create a different request model for data validation
- Field data validation on each variable/element.
 
 # Different validations
 - Field validation to validate the POST and PUT methods
 - Path validation for path parameters in GET nad DELETE methods
 - Query validation for query parameters in GET and DELETE methods

 # Error handling
 - Status Codes
   - An HTTP Status Code is used to help the Client (the user or system submitting data to the server) to understand what happened on the server side application.
   - Status Code are international standards on how a Client/Server should handle the result of a request
   - It allows everyone who sends a request to know if their submission was successful or not.
   - Common Status Codes:
    - 1xx : Information Response: Request processing.
    - 2xx : Sccess: Request Successfully complete
    - 3xx : Redirection: Further action must be completed
    - 4xx : Client Errors: An Error was caused by the client
    - 5xx : Server Errors: An error occured on the server.

   - 200: OK (GET)
   - 201: Created (POST)
   - 204: No Content (PUT)

   - 400: Bad Request --> Cannot process request due to client error. Commonly used for invalid request methods.
   - 401: Unauthorized --> Client does not have valid authentication for target resource
   - 404: Not Found --> The clients requested resource cannot be found.
   - 422: Unprocessable Entity --> Semantic Errors in Client request

   - 500: Internal Server Error --> Generic Error Message, when an unexpected issue on te server happened.

  - Explicit Status Code response
  - Example:
    from starlette import status
    @app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)