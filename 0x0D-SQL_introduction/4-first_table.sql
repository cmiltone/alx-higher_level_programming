-- script shows full of 'first_table' table description for a database passed via command line
DROP TABLE IF EXISTS first_table;
CREATE TABLE first_table (
  id INTEGER
  name VARCHAR(256)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
