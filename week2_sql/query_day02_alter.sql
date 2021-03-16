CREATE DATABASE alexis_db;
USE alexis_db;

-- first digit in identity denotes the start value
-- second deigit denotes the 'increment by' value
CREATE TABLE film_table 
(
    film_id INT IDENTITY(1,1) PRIMARY KEY,
    film_name VARCHAR(10) NOT NULL,
    film_type VARCHAR(6),
)

SP_HELP film_table;

INSERT INTO film_table
VALUES
('Batman 2', 'Action'),
('Superman', null)

SELECT * FROM film_table;

INSERT INTO film_table
(film_type, film_name)
VALUES
('Sci-fi', 'Mandalori'),
('Sci-fi', 'Star Wars'),
('Sci-fi', 'Star Trek');

-- Delete duplicate films by erasing films with id larger than 6
DELETE FROM film_table WHERE film_id > 6;

-
-- EXEC sp_fkeys 'film_table'

-- Cascade delete


-- Update value to not null
UPDATE film_table SET film_type = 'Action' WHERE film_id=5;
-- Alter column to reject null values
ALTER TABLE film_table ALTER COLUMN film_type VARCHAR(10) NOT NULL; 
-- Alternatively, add default value to film type
ALTER TABLE film_table ADD CONSTRAINT df_film_type DEFAULT 'Sci-fi' FOR film_type;
-- Drop default value
ALTER TABLE film_table 
ALTER COLUMN film_type DROP DEFAULT; -- Doesn't work

INSERT INTO film_table VALUES ('Clone Wars');

SP_HELP film_table;