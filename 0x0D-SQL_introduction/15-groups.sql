-- script lists number of records with same score
SELECT `score`, COUNT(DISTINCT `score`) as `number` FROM `second_table` GROUP BY score ORDER BY score DESC;
