-- creates the database hbtn_0d_usa and the table cities
DROP TABLE IF EXISTS force_name;
CREATE TABLE force_name (
  id INTEGER DEFAULT 1 UNIQUE AUTO_INCREMENT PRIMARY KEY,
  state_id INT NOT NULL,
  name VARCHAR(256) NOT NULL,
  FOREIGN KEY (state_id) REFERENCES states(id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
