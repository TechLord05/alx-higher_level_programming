-- This script creates the MySQL database 'hbtn_0d_2' and the user 'user_0d_2'.
-- The user 'user_0d_2' is granted SELECT privilege on the database 'hbtn_0d_2'.

-- Creating database hbtn_0d_2 if it doesn't exist
-- Creating user_0d_2 with SELECT privilege on hbtn_0d_2
-- Refreshing privileges
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

FLUSH PRIVILEGES;
