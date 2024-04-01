-- Script to get the environment ready, it creates a database
-- And a new user with the required privileges
-- Creates the database hbnb_test_db in my MySQL server.
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;
-- creates the MySQL server user hbnb_dev
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Set hbnb_test privileges
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
