-- Schema for all of the staging tables
CREATE SCHEMA IF NOT EXISTS staging;

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

CREATE TABLE IF NOT EXISTS staging.title_crew (
    tconst TEXT,
    directors TEXT,
    writers TEXT
)

CREATE TABLE IF NOT EXISTS staging.name_basics (
    nconst TEXT
)

