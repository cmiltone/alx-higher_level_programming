-- script displays avg teperature by city ordered by temperature (desc)
SELECT DISTINCT `city`, AVG(`value`) as `avg_temp` FROM `temperatures` GROUP BY city ORDER BY avg_temp DESC;
