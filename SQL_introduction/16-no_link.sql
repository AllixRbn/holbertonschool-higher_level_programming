-- Lists all records of the table second_table where the name is not null, ordered by score in descending order.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
