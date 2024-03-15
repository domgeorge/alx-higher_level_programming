-- script creates the table
-- unique_id on MySQL server
CREATE TABLE IF NOT EXISTS unique_id
-- id INT with default value 1 and must be unique
(id INT DEFAULT 1 UNIQUE,
-- name VARCHAR(256)
name VARCHAR(256));
