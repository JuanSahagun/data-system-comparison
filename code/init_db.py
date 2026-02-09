"""
Initialize the database by creating the necesary tables.
"""
import psycopg
from pathlib import Path

SCHEMA_FILES = ["staging-schemas.sql"]
SCHEMA_DIR = Path(__file__).resolve().parent / "table-schemas"

def run_sql(cur: psycopg.Cursor, path: Path) -> None:
    cur.execute(path.read_text(encoding="utf-8"))

def main() -> None:
    # Connect to the database
    with psycopg.connect("postgresql://localhost/moviedb") as con:
        # Open a cursor to perform the db operations
        with con.cursor() as cur:
            # Set the search path to the 'public' schema 
            cur.execute("SET search_path TO public;")
            # Create the staging tables
            for file in SCHEMA_FILES:
                run_sql(cur, SCHEMA_DIR / file)
        # Comit any pending trasnaction to the db
        con.commit()


if __name__ == "__main__":
    main()
