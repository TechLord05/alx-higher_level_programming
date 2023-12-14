-- Creating the database hbtn_0d_usa if it does not exist
-- Using the database hbtn_0d_usa
-- Creating the table cities with id as a unique, auto-generated, non-null primary key,
-- state_id as a non-null FOREIGN KEY referencing the id column of the states table,
-- and name as a non-null VARCHAR(256)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);

