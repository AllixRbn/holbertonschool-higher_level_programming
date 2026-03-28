-- Creates the table unique_id in the database hbtn_0d_2 with the following columns:
-- id: INT with the default value 1 and UNIQUE constraint
-- name: VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
