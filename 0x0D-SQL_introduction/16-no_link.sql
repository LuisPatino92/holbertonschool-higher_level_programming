-- List all the entries of second_table avoiding entries with no name
-- The database name should be especified in the calling of the script

SELECT `score`, `name` FROM second_table WHERE `name` <> '' ORDER BY `score` DESC
