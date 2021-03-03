-- Computes the frequency table for the scores
-- The database name should be especified in the calling of the script

SELECT `score`, COUNT(*) AS `number` FROM second_table GROUP BY `score` ORDER BY `score` DESC
