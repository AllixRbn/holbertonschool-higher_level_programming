-- Creates the database hbtn_0d_usa with the following columns and constraints:
-- id: INT with the AUTO_INCREMENT and PRIMARY KEY constraints
-- name: VARCHAR(256) with the NOT NULL constraint
-- state_id: INT with the NOT NULL constraint and a FOREIGN KEY constraint that references the id column of the states table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
