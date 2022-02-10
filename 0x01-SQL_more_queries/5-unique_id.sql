-- creates a table -> 'unique_id'
-- <attributes>: id, name -> values/types = INT(default=1 & unique), VARCHAR256
CREATE TABLE IF NOT EXISTS unique_id(id INT default 1 UNIQUE, name VARCHAR(256));
