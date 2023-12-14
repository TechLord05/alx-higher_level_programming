-- Listing all records with a name value in the table second_table
-- Displaying the score and the name, ordered by descending score

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
