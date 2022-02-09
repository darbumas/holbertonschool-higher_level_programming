-- lists all records in table 'second_table' from db hbtn-0c_0
-- excludes rows without a name value
SELECT score, name FROM second_table WHERE name IS NOT NULL
ORDER BY score DESC;
