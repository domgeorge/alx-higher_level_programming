-- Script lists all records of table
-- second_table of database hbtn_0c_0
-- Don’t list rows without a name value
-- Results will display the score and the name
SELECT score, name FROM second_table
WHERE name IS NOT NULL ORDER BY score DESC;
