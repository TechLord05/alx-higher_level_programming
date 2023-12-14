-- Creating the table id_not_null with id having a default value of 1 and name column
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
