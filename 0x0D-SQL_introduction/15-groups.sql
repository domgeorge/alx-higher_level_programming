-- Script that lists the number of records with the same score in the table
-- second_table of database hbtn_0c_0
-- list should be sorted by number of records (descending)
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
