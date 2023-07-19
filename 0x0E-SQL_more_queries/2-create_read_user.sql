-- script crestes db and user
DROP DATABASE IF EXISTS hbtn_0d_2;
CREATE DATABASE hbtn_0d_2;
use hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
ALTER USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_2'@localhost;
FLUSH PRIVILEGES;
