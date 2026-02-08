import psycopg

conn = psycopg.connect("postgresql://localhost/moviedb")
# Create a cursor object
cur = conn.cursor()

# Create a first test table for movies
cur.execute("""
    CREATE TABLE IF NOT EXISTS title_test (
        tconst TEXT PRIMARY KEY,
        ptitle TEXT NOT NULL,
        releaseYear INTEGER,
            CONSTRAINT valid_year CHECK (
                releaseYear BETWEEN 1888 AND 9999
            )
    )     
""")

# Add a couple of tuples
cur.execute("""
    INSERT INTO title_test (tconst, ptitle, releaseYear) VALUES
            ('AX007', 'Eternal Sunshine of the Spotless Mind', 2007),
            ('XQ909', 'Avatar: Fire and Ash', 2026)
""")

# Insert data from a list
more_movies = [
    ('JD880', 'Parasite', 2019),
    ('LK0222', 'No Other Choice', 2026),
    ('HB182', 'Whiplash', 2015)
]
# Use executemany to insert multiple tuples
cur.executemany(
    "INSERT INTO title_test (tconst, ptitle, releaseYear) VALUES (%s, %s, %s)",
    more_movies
)
# Commit the transaction
conn.commit()
# Close the cursor and connection
cur.close()
conn.close()
