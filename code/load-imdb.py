import psycopg
import gzip
from pathlib import Path

IMDB_FILES = ["title.basics.tsv.gz"]
DATA_DIR = Path(__file__).parents[1] / "data"

copy_sql = """
COPY staging.title_basics
FROM STDIN
WITH (FORMAT text, DELIMITER E'\\t', NULL '\\N');
"""

def main() -> None:
    with psycopg.connect("postgresql://localhost/moviedb") as conn:
        # Truncate the table before loading, to prevent duplicate tuples
        with conn.cursor() as cur:
            cur.execute("TRUNCATE staging.title_basics;")
        
        # Load the dataset into the staging table
        with conn.cursor() as cur, cur.copy(copy_sql) as copy:
            with gzip.open(DATA_DIR/IMDB_FILES[0], "rt", encoding="utf-8", newline="") as f:
                # Manually skip the header line
                next(f)
                for line in f:
                    copy.write(line)

if __name__ == "__main__":
    main()

# with psycopg.connect("postgresql://localhost/moviedb") as conn:
#     with conn.cursor() as cur, cur.copy(copy_sql) as copy:
#         with gzip.open(DATA_DIR/IMDB_FILES[0], "rt", encoding="utf-8") as f:
#             for line in f:
#                 copy.write(line)
