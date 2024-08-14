# Alembic

- Alembic is a powerful migration tool that allows us to modify our database schemas.
- As our application evolves, our database will need to evolve as well.
- Alembic helps us to able to keep modifying out database to keep up with rapid development requirements.

# Alembic commands

- `alembic inti <folder_name>` : Initialize a new, generic env
- `alembic revision -m <message>` : Creates a new revision of the env
- `alembic upgrade <revision #>` : Run our upgrade migration to our database
- `alembic downupgrade -1` : Run our downupgrade migration to our database

# How do Alembic work?
- After we initialize our project with alembic, 2 new items will appear in our directory
    - alembic.ini
    - alembic directory
        - Has all env properties for alembic
        - Holds all revisions of our application
        - where you can call the migrations for upgrading
        - where you can call the migrations for downupgrading
- These are created automatically by alembic so we can upgrade, downgrade and keep data integrity of our application.

# Alembic Revision
- Alembic revision is how we create a new alembic file where we can add some type of database upgrade.
- When we run:
    `alembic revision -m "create phone number col on user table"
- Creates a new file where we can write the upgrade code
- Each new revision will have a Revision ID
