-- lists the number of records from 'second_table' with same score
-- results display the score and number of records with the same score
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score
ORDER BY number DESC;
