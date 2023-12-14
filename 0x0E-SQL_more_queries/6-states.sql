-- Creating the database hbtn_0d_usa if it does not exist
-- Using the database hbtn_0d_usa
-- Creating the table states with id as a unique, auto-generated, non-null primary key
-- and name as a non-null VARCHAR(256)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

