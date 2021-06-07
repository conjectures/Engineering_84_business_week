-- SQL Mini Project PART 2
-- Alexis Othonos

CREATE DATABASE alexis_db
USE alexis_db

create table spartans_table (
    sparta_id INT IDENTITY(1,1) PRIMARY KEY,
    title VARCHAR(4),
    first_name VARCHAR(10),
    last_name VARCHAR(10),
    university VARCHAR(15),
    date_enrolled DATE,
    course_code CHAR(6),
    mark INT
)

INSERT INTO spartans_table 
    VALUES
    ('Mr.', 'John', 'Smith', 'UCL', '10/1/2016', 'ECE456', 60),
    ('Ms.', 'Mary', 'Johnson', 'CAL', '10/2/2015', 'PHY213', 73),
    ('Dr.', 'Peter', 'Lowe', 'UoE', '09/28/2018', 'CS-112', 77 )


-- SELECT * FROM spartans_table
-- DROP TABLE spartans_table