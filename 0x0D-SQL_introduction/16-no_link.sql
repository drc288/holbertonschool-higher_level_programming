-- verify if the name is not null
SELECT score, name
FROM second_table
WHERE name is not NULL
ORDER BY score DESC;
