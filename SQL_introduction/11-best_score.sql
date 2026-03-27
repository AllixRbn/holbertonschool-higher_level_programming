-- List the scores in the `second_table` table that are greater than or equal to 10, sorted from highest to lowest
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
