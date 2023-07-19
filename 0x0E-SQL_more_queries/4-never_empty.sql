-- script creates the table id_not_null
DROP TABLE IF EXISTS force_name;
CREATE TABLE force_name (
  id INTEGER DEFAULT 1,
  name VARCHAR(256)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
