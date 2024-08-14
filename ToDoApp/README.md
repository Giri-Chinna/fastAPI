# Project #
- This will include"
    * Full SQL Database
    * Authentication
    * Authorization
    * Hashing Passwords

# TODOS PROJECT
- We will create new Todo table models for our application
- We will be using these Todos to save records throughout this project.

# Authorization and Authentication            Retrieving the user and saving Todos
`Web Page <----------------------> Fast API <-----------------------> Databases`


# Routers


# JWT
- JSON WEB TOKEN
- JWT is a self-contained way to securely transmit data and information between 2 parties using JSON Object.
- JWTs can be trusted because each JWT can be digitally signed, which in return allows server to know if the JWT has been chnaged at all.
- JWT should be used when dealing with authorization.
- JWT is a great way for information to be exchanged between the server and the client.

# JWT Structure
- A JSON Wen Token is created of 3 separate parts separated by dots(.) which includes:
    - Header: (a)
        - A JWT header usually consist of 2 parts:
            - "alg" The algorithm for signing
            - "typ" The specific type of token
            {
                "alg": "HS256",
                "typ": "JWT"
            }
        - The JWT header is then encoded using Base64 to create the first part of the JWT (a)
    - Payload: (b)
        - A JWT Payload consists of the data.
        - The Payload data constains claims, and there are 3 different types of claims:
            - Registered
                - iss
                - sub
                - expire
            - Public
            - Private
        - The JWT payload is then encoded using Base64 to create the second part of the JWT (b)
    - Signature: (c) 
        - A JWT Signature is created by using the algorithm in the header to hash out the encoded headed, encoded payload with a secret.
        - The secret can be anything, but is saved somewhere on the server that the client does not have access to.
        - The signature is the third and final part of a JWT (c)
        HMACSHA256(
            base64UrlEncode(header) + "." +
            base64UrlEncode(payload),
            ssecret
        )

