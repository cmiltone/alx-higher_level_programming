-- script displays max temp of each state
SELECT DISTINCT `state`, MAX(`value`) as `max_temp` FROM `temperatures` GROUP BY state ORDER BY state;
