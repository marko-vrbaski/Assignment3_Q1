# Assignment3_Q1
For school project

VIDEO LINK: https://www.youtube.com/watch?v=Y1lpqLCoZrI


CREATING TABLE ---------------

!! Or use the database script I provided called -> databaseScript.sql

Query for creating the table:

CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE
);

Query for inserting inital Values:

INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');

CONNECTING TO POSTGRE --------------------

In the json file make changes to the following,
DB_NAME: is the name of the database you have created, 
DB_USER: username of database, most likely [ postgres ]
DB_PASS: your password for the database,
DB_HOST: host name, most likely [ localhost ]
DB_PORT: port , most likely [ 5432 ]

make sure in the Assignment_3_Q1.py file that the name of your json file is the same as the name of the file you are trying to read

-> also make sure that psycopg2 library is installed, COMMAND TO INSTALL: pip install psycopg2-binary

Finally run the program and follow the input prompts 

