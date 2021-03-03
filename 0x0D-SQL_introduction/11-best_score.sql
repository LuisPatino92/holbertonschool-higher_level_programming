-- Lists all the records of second_table ordered by score where score >= 10
-- The database name should be especified in the calling of the script

SELECT `score`, `name` FROM second_table WHERE `score` >= 10 ORDER BY `score` DESC;
