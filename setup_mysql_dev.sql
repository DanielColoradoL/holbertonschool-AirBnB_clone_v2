-- Script to get the environment ready, it creates a database
-- And a new user with the required privileges
-- Creates the database hbtn_0c_0 in my MySQL server.
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;
-- creates the MySQL server user hbnb_dev
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Set hbnb_dev privileges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
