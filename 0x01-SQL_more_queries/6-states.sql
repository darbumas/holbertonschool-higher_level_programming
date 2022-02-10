-- creates a database -> 'hbtn_0d_usa' with table -> 'states'
-- <attributes>: id, name -> values/types: INT(uniq, auto-gen, not null)
--					   VARCHAR(256, not null)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
	);
