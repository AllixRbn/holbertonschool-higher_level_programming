-- Creates the database hbtn_0d_usa and the table states with the following columns:
-- id: INT with the AUTO_INCREMENT and PRIMARY KEY constraints
-- name: VARCHAR(256) with the NOT NULL constraint
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
