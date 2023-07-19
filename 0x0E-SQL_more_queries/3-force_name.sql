-- script creates the table force_name
DROP TABLE IF EXISTS force_name;
CREATE TABLE force_name (
  id INTEGER,
  name VARCHAR(256)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
