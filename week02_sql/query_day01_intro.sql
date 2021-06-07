
CREATE DATABASE alexis_db;
USE alexis_db;

-- first digit in identity denotes the start value
-- second deigit denotes the 'increment by' value
CREATE TABLE film_table 
(
    film_id INT IDENTITY(1,1) PRIMARY KEY,
    film_name VARCHAR(10),
    film_type VARCHAR(6),
)

SP_HELP film_table;

INSERT INTO film_table
VALUES
('Batman 2', 'Action'),
('Superman', 'Action')

SELECT * FROM film_table;

INSERT INTO film_table
(film_type, film_name)
VALUES
('Sci-fi', 'Mandalori'),
('Sci-fi', 'Star Wars'),
('Sci-fi', 'Star Trek')

DELETE FROM film_table WHERE film_id > 6;

-- sgiw fireugb jets
EXEC sp_fkeys 'film_table'

-- Cascade delete
