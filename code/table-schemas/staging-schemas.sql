-- Schema for all of the staging tables
CREATE SCHEMA IF NOT EXISTS staging;

-- Titles and basic info about them
CREATE TABLE IF NOT EXISTS staging.title_basics (
    tconst TEXT,
    titleType TEXT,
    primaryTitle TEXT,
    originalTitle TEXT,
    isAdult TEXT,
    startYear TEXT,
    endYear TEXT,
    runtimeMinutes TEXT,
    genres TEXT
)

-- The writers and directors of a title
CREATE TABLE IF NOT EXISTS staging.title_crew (
    tconst TEXT,
    directors TEXT,
    writers TEXT
)

-- People info
CREATE TABLE IF NOT EXISTS staging.name_basics (
    nconst TEXT,
    primaryName TEXT,
    birthYear TEXT,
    deathYear TEXT,
    primaryProfession TEXT,
    knownForTitles TEXT
)

