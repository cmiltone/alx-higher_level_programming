-- script creates table 'second_table'
DROP TABLE IF EXISTS second_table;
CREATE TABLE second_table (
  id INTEGER,
  name VARCHAR(256),
  score INTEGER
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, 'John', 10),(2, 'Alex', 3),(3, 'Bob', 14),(4, 'George', 8);